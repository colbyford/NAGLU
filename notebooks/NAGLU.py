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
assembler = VectorAssembler(inputCols = assemblerInputs, outputCol="features")
stages += [assembler]

prepPipeline = Pipeline().setStages(stages)
pipelineModel = prepPipeline.fit(dataset)
dataset = pipelineModel.transform(dataset)

display(dataset)

## Save Transformation Pipeline
# pipelineModel.save("/mnt/trainedmodels/pipeline")
# display(dbutils.fs.ls("/mnt/trainedmodels/pipeline"))

## Read in Transformation Pipeline
# from pyspark.ml import PipelineModel
# pipelineModel = PipelineModel.load("/mnt/trainedmodels/pipeline")
# dataset = pipelineModel.transform(dataset)
# display(dataset)

# COMMAND ----------

