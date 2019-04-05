# Prediction of the Effect of Naturally Occurring Missense Mutations on Cellular N-Acetyl-Glucosaminidase Enzymatic Activity

<p align="right">C. T. Ford, C. M. Nodzak, A. Uppal, and X. Shi<br><i>The University of North Carolina at Charlotte, Dept. of Bioinformatics and Genomics</i></p>

### [View Article on _bioRxiv_.](https://www.biorxiv.org/content/10.1101/598870v1)

## Abstract
In 2015, the Critical Assessment of Genome Interpretation (CAGI) proposed a challenge to devise a computational method for predicting the phenotypic consequences of genetic variants of a lysosomal hydrolase enzyme known as $\alpha$-N-acetylglucosaminidase (NAGLU). In 2014, the Human Gene Mutation Database released that 153 NAGLU mutations associated with MPS IIIB and 90 of them are missense mutations. The ExAC dataset catalogued 189 missense mutations NAGLU based on exome sequence data from about 60,000 individual and 24 of them are known to be disease associated. Biotechnology company, BioMarin, has quantified the relative functionality of NAGLU for the remaining subset of 165 missense mutations. For this particular challenge, we examined the subset missense mutations within the ExAC dataset and predicted the probability of a given mutation being deleterious and relating this measure to the capacity of enzymatic activity. In doing so, we hoped to learn the degree to which changes in amino acid physicochemical properties are tolerable for NAGLU function.

Amino acid substitution (AAS) prediction methods are mainly based on the sequence and structure information. Simple comparisons between different AAS methods are not only difficult, but also irrational because each method was tested on various datasets and based on varied versions of databases. Currently, several AAS prediction methods have been introduced. PolyPhen-2, an updated version of PolyPhen, is a tool used to predict possible impacts of an amino acid substitution on the structure and function. Users are required to provide protein or SNP identifiers, protein sequences, substitution positions, etc. A score is provided, ranging from 0 to 1, corresponding to the probability of a mutation resulting in no functionality for the enzyme

Once the probability scores were generated, the dataset was then run through multiple machine learning algorithms to generate an applicable model for predicting the enzymatic activity of MPS IIIB-related mutations. This prediction was generated using the PolyPhen-2 probability score and other information about the mutation (amino acid type, location, allele frequency, etc.) as input feature variables. This generated a predicted aggregate score for each mutation, which was then reported back to CAGI. The results of the analysis are significant enough to hold confidence that the scores are decent predictors of enzymatic activity given a mutation in the NAGLU amino acid sequence.

## How to Cite


```
Prediction of the Effect of Naturally Occurring Missense Mutations on Cellular N-Acetyl-Glucosaminidase Enzymatic Activity
Colby T Ford, Conor M Nodzak, Aneeta Uppal, Xinghua Shi
bioRxiv 598870; doi: https://doi.org/10.1101/598870 
```

### BibTex:
```
@article {NAGLU,
	author = {Ford, Colby T. and Nodzak, Conor M. and Uppal, Aneeta and Shi, Xinghua},
	title = {Prediction of the Effect of Naturally Occurring Missense Mutations on Cellular N-Acetyl-Glucosaminidase Enzymatic Activity},
	elocation-id = {598870},
	year = {2019},
	doi = {10.1101/598870},
	publisher = {Cold Spring Harbor Laboratory},
	abstract = {In 2015, the Critical Assessment of Genome Interpretation (CAGI) proposed a challenge to devise a computational method for predicting the phenotypic consequences of genetic variants of a lysosomal hydrolase enzyme known as α-N-acetylglucosaminidase (NAGLU). In 2014, the Human Gene Mutation Database released that 153 NAGLU mutations associated with MPS-IIIB and 90 of them are missense mutations. The ExAC dataset catalogued 189 missense mutations NAGLU based on exome sequence data from about 60,000 individual and 24 of them are known to be disease associated. Biotechnology company, BioMarin, has quantified the relative functionality of NAGLU for the remaining subset of 165 missense mutations. For this particular challenge, we examined the subset missense mutations within the ExAC dataset and predicted the probability of a given mutation being deleterious and relating this measure to the capacity of enzymatic activity. In doing so, we hoped to learn the degree to which changes in amino acid physicochemical properties are tolerable for NAGLU function. Amino acid substitution (AAS) prediction methods are mainly based on the sequence and structure information. Simple comparisons between different AAS methods are not only difficult, but also irrational because each method was tested on various datasets and based on varied versions of databases. Currently, several AAS prediction methods have been introduced. PolyPhen-2, an updated version of PolyPhen, is a tool used to predict possible impacts of an amino acid substitution on the structure and function. Users are required to provide protein or SNP identifiers, protein sequences, substitution positions, etc. A score is provided, ranging from 0 to 1, corresponding to the probability of a mutation resulting in no functionality for the enzyme. Once the probability scores were generated, the dataset was then run through multiple machine learning algorithms to generate an applicable model for predicting the enzymatic activity of MPS IIIB-related mutations. This prediction was generated using the PolyPhen-2 probability score and other information about the mutation (amino acid type, location, allele frequency, etc.) as input feature variables. This generated a predicted aggregate score for each mutation, which was then reported back to CAGI. The results of the analysis are significant enough to hold confidence that the scores are decent predictors of enzymatic activity given a mutation in the NAGLU amino acid sequence.},
	URL = {https://www.biorxiv.org/content/early/2019/04/05/598870},
	eprint = {https://www.biorxiv.org/content/early/2019/04/05/598870.full.pdf},
	journal = {bioRxiv}
}

```
