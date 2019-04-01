# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM naglu_data

# COMMAND ----------

from pyspark.sql import *
from pyspark.sql.functions import col

dataset = spark.table("naglu_data").select(col("allele1"),
                                        col("chromosome"),
                                        col("variant_position"),
                                        col("AA_substitution"),
                                        col("cDNA_nucleotide_change"),
                                        col("AA_reference"),
                                        col("allele2"),
                                        col("prediction"),
                                        col("pph2_class"),
                                        col("pph2_prob"),
                                        col("pph2_FPR"),
                                        col("pph2_TPR"),
                                        col("pph2_FDR"),
                                        col("allele3"))

display(dataset)

# COMMAND ----------

from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, OneHotEncoderEstimator, StringIndexer, VectorAssembler

label = "pph2_prob"
categoricalColumns = ["allele1",
                      "allele2",
                      #"allele3",
                      #"chromosome",
                      "variant_position",
                      "AA_substitution",
                      "cDNA_nucleotide_change",
                      "AA_reference",
                      "prediction",
                      "pph2_class"]

numericalColumns = ["pph2_FPR",
                    "pph2_TPR",
                    "pph2_FDR"]

# categoricalColumnsclassVec = ["col1classVec",
#                               "col2classVec"]

categoricalColumnsclassVec = [c + "classVec" for c in categoricalColumns]
print(categoricalColumnsclassVec)

# COMMAND ----------

from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler
stages = []

for categoricalColumn in categoricalColumns:
  print(categoricalColumn)
  # Category Indexing with StringIndexer
  stringIndexer = StringIndexer(inputCol=categoricalColumn, outputCol = categoricalColumn+"Index").setHandleInvalid("skip")
  # Use OneHotEncoder to convert categorical variables into binary SparseVectors
  encoder = OneHotEncoder(inputCol=categoricalColumn+"Index", outputCol=categoricalColumn+"classVec")
  # Add stages.  These are not run here, but will run all at once later on.
  stages += [stringIndexer, encoder]

# Convert label into label indices using the StringIndexer
#label_stringIndexer = StringIndexer(inputCol = label, outputCol = "label").setHandleInvalid("skip")
#stages += [label_stringIndexer]

# Transform all features into a vector using VectorAssembler
assemblerInputs = categoricalColumnsclassVec + numericalColumns
assembler = VectorAssembler(inputCols = assemblerInputs, outputCol="features").setHandleInvalid("skip")
stages += [assembler]

prepPipeline = Pipeline().setStages(stages)
pipelineModel = prepPipeline.fit(dataset)
dataset = pipelineModel.transform(dataset)

display(dataset)


# COMMAND ----------


## Save Transformation Pipeline
pipelineModel.save("/mnt/general/trainedmodels/NAGLU/pipeline")
display(dbutils.fs.ls("/mnt/general/trainedmodels/NAGLU/pipeline"))

## Read in Transformation Pipeline
# from pyspark.ml import PipelineModel
# pipelineModel = PipelineModel.load("/mnt/trainedmodels/pipeline")
# dataset = pipelineModel.transform(dataset)
# display(dataset)

# COMMAND ----------

# Keep relevant columns
cols = ["variant_position", "AA_substitution", "pph2_prob"]
selectedcols = ["features"] + cols
dataset = dataset.select(selectedcols)
dataset.printSchema()

# COMMAND ----------

#Split Data into Train and Test sets
# train, test = dataset.randomSplit([0.75, 0.25], seed=1337)
# print("Train: ", train.count())
# print("Test: ", test.count())

## Use full dataset to train
train = dataset
test = dataset

display(train)

# COMMAND ----------

# DBTITLE 1,Linear Regression
from pyspark.ml.regression import LinearRegression
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.mllib.evaluation import BinaryClassificationMetrics
#from mmlspark import ComputeModelStatistics

# Create initial LinearRegression model
lr = LinearRegression(labelCol="pph2_prob", featuresCol="features")


# Create ParamGrid for Cross Validation
lrparamGrid = (ParamGridBuilder()
             .addGrid(lr.regParam, [0.001, 0.01, 0.1, 0.2, 0.5, 1.0, 2.0])
             .addGrid(lr.elasticNetParam, [0.0, 0.1, 0.25, 0.5, 0.75, 1.0])
             .addGrid(lr.maxIter, [1, 5, 10, 20, 50, 100])
             .build())

# Evaluate model
lrevaluator = RegressionEvaluator(predictionCol="prediction", labelCol="pph2_prob", metricName="rmse")

# Create 5-fold CrossValidator
lrcv = CrossValidator(estimator = lr,
                    estimatorParamMaps = lrparamGrid,
                    evaluator = lrevaluator,
                    numFolds = 5)

# Run cross validations
lrcvModel = lrcv.fit(train)
print(lrcvModel)

# Get Model Summary Statistics
lrcvSummary = lrcvModel.bestModel.summary
#print("Coefficient Standard Errors: " + str(lrcvSummary.coefficientStandardErrors))
#print("P Values: " + str(lrcvSummary.pValues)) # Last element is the intercept

# Use test set here so we can measure the accuracy of our model on new data
lrpredictions = lrcvModel.transform(test)

# cvModel uses the best model found from the Cross Validation
# Evaluate best model
print('RMSE:', lrevaluator.evaluate(lrpredictions))

# COMMAND ----------

# DBTITLE 1,Random Forest
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import RegressionEvaluator

# Create an initial RandomForest model.
rf = RandomForestRegressor(labelCol="pph2_prob", featuresCol="features")

# Evaluate model
rfevaluator = RegressionEvaluator(predictionCol="prediction", labelCol="pph2_prob", metricName="rmse")

# Create ParamGrid for Cross Validation
rfparamGrid = (ParamGridBuilder()
             .addGrid(rf.maxDepth, [2, 5, 10, 20, 30])
             .addGrid(rf.maxBins, [10, 20, 40, 80, 100])
             .addGrid(rf.numTrees, [5, 20, 50, 100, 500, 10000])
             .build())

# Create 5-fold CrossValidator
rfcv = CrossValidator(estimator = rf,
                      estimatorParamMaps = rfparamGrid,
                      evaluator = rfevaluator,
                      numFolds = 5)

# Run cross validations.
rfcvModel = rfcv.fit(train)
print(rfcvModel)

# Use test set here so we can measure the accuracy of our model on new data
rfpredictions = rfcvModel.transform(test)

# cvModel uses the best model found from the Cross Validation
# Evaluate best model
print('RMSE:', rfevaluator.evaluate(rfpredictions))

# COMMAND ----------

# DBTITLE 1,Gradient Boosted Tree
from pyspark.ml.regression import GBTRegressor
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import RegressionEvaluator

# Create initial Decision Tree Model
gt = GBTRegressor(labelCol="pph2_prob", featuresCol="features")

# Create ParamGrid for Cross Validation
gtparamGrid = (ParamGridBuilder()
             .addGrid(gt.maxDepth, [2, 5, 10, 20, 30])
             #.addGrid(gt.maxDepth, [2, 5, 10])
             .addGrid(gt.maxBins, [10, 20, 40, 80, 100])
             #.addGrid(gt.maxBins, [10, 20])
             .build())

# Evaluate model
gtevaluator = RegressionEvaluator(predictionCol="prediction", labelCol="pph2_prob", metricName="rmse")

# Create 5-fold CrossValidator
gtcv = CrossValidator(estimator = gt,
                      estimatorParamMaps = gtparamGrid,
                      evaluator = gtevaluator,
                      numFolds = 5)

# Run cross validations
gtcvModel = gtcv.fit(train)
print(gtcvModel)

# Use test set here so we can measure the accuracy of our model on new data
gtpredictions = gtcvModel.transform(test)

# cvModel uses the best model found from the Cross Validation
# Evaluate best model
print('RMSE:', gtevaluator.evaluate(gtpredictions))

# COMMAND ----------

# DBTITLE 1,Decision Tree
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import RegressionEvaluator

# Create initial Decision Tree Model
dt = DecisionTreeRegressor(labelCol="pph2_prob", featuresCol="features")

# Create ParamGrid for Cross Validation
dtparamGrid = (ParamGridBuilder()
             .addGrid(dt.maxDepth, [2, 5, 10, 20, 30])
             #.addGrid(dt.maxDepth, [2, 5, 10])
             .addGrid(dt.maxBins, [10, 20, 40, 80, 100])
             #.addGrid(dt.maxBins, [10, 20])
             .build())

# Evaluate model
dtevaluator = RegressionEvaluator(predictionCol="prediction", labelCol="pph2_prob", metricName="rmse")

# Create 5-fold CrossValidator
dtcv = CrossValidator(estimator = dt,
                      estimatorParamMaps = dtparamGrid,
                      evaluator = dtevaluator,
                      numFolds = 5)

# Run cross validations
dtcvModel = dtcv.fit(train)
print(dtcvModel)

# Use test set here so we can measure the accuracy of our model on new data
dtpredictions = dtcvModel.transform(test)

# cvModel uses the best model found from the Cross Validation
# Evaluate best model
print('RMSE:', dtevaluator.evaluate(dtpredictions))

# COMMAND ----------

# DBTITLE 1,Evaluate Models
print('Linear Regression RMSE:', lrevaluator.evaluate(lrpredictions))
print('Random Forest RMSE:', rfevaluator.evaluate(rfpredictions))
print('Gradient Boosted Tree RMSE:', gtevaluator.evaluate(gtpredictions))
print('Decision Tree RMSE:', dtevaluator.evaluate(dtpredictions))

# COMMAND ----------

allpredictions = lrpredictions.withColumnRenamed("prediction", "lr_prediction") \
                              .join(rfpredictions.withColumnRenamed("prediction", "rf_prediction"), ["variant_position", "AA_substitution", "pph2_prob", "features"]) \
                              .join(gtpredictions.withColumnRenamed("prediction", "gt_prediction"), ["variant_position", "AA_substitution", "pph2_prob", "features"]) \
                              .join(dtpredictions.withColumnRenamed("prediction", "dt_prediction"), ["variant_position", "AA_substitution", "pph2_prob", "features"])

display(allpredictions)

# COMMAND ----------

display(dbutils.fs.ls("/mnt/"))

# COMMAND ----------

## Write Model to Blob
lrcvModel.save("/mnt/general/trainedmodels/NAGLU/lr")
rfcvModel.save("/mnt/general/trainedmodels/NAGLU/rf")
gtcvModel.save("/mnt/general/trainedmodels/NAGLU/gt")
dtcvModel.save("/mnt/general/trainedmodels/NAGLU/dt")
display(dbutils.fs.ls("/mnt/general/trainedmodels/NAGLU"))

# COMMAND ----------


