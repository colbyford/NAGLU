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

```latex
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
---------------------------

# Article in _Human Mutation_: Assessment of predicted enzymatic activity of alpha‐N‐acetylglucosaminidase (NAGLU) variants of unknown significance for CAGI 2016
This work was combined with other researchers for CAGI 2016 and published as a compilation article in _Human Mutation_.

### [View Article in _Human Mutation_.](https://onlinelibrary.wiley.com/doi/pdf/10.1002/humu.23875)

## How to Cite

```latex
Clark, W. T., Kasak, L. , Bakolitsa, C. , Hu, Z. , Andreoletti, G. ,
Babbi, G. , Bromberg, Y. , Casadio, R. , Dunbrack, R. , Folkman, L. ,
Ford, C. T., Jones, D. , Katsonis, P. , Kundu, K. , Lichtarge, O. ,
Martelli, P. L., Mooney, S. D., Nodzak, C. , Pal, L. R., Radivojac, P. ,
Savojardo, C. , Shi, X. , Zhou, Y. , Uppal, A. , Xu, Q. , Yin, Y. ,
Pejaver, V. , Wang, M. , Wei, L. , Moult, J. , Yu, G. K., Brenner, S. E. and LeBowitz, J. H.
(2019), Assessment of predicted enzymatic activity of alpha‐N‐acetylglucosaminidase (NAGLU)
variants of unknown significance for CAGI 2016. Human Mutation.
Accepted Author Manuscript. doi:10.1002/humu.23875
```


### BibTex:
```latex
@article{doi:10.1002/humu.23875,
author = {Clark, Wyatt T. and Kasak, Laura and Bakolitsa, Constantina and Hu, Zhiqiang and Andreoletti, Gaia and Babbi, Giulia and Bromberg, Yana and Casadio, Rita and Dunbrack, Roland and Folkman, Lukas and Ford, Colby T. and Jones, David and Katsonis, Panagiotis and Kundu, Kunal and Lichtarge, Olivier and Martelli, Pier Luigi and Mooney, Sean D. and Nodzak, Conor and Pal, Lipika R. and Radivojac, Predrag and Savojardo, Castrense and Shi, Xinghua and Zhou, Yaoqi and Uppal, Aneeta and Xu, Qifang and Yin, Yizhou and Pejaver, Vikas and Wang, Meng and Wei, Liping and Moult, John and Yu, G. Karen and Brenner, Steven E. and LeBowitz, Jonathan H.},
title = {Assessment of predicted enzymatic activity of alpha-N-acetylglucosaminidase (NAGLU) variants of unknown significance for CAGI 2016},
journal = {Human Mutation},
volume = {},
number = {},
pages = {},
keywords = {alpha-N-acetylglucosaminidase, CAGI, critical assessment, enzymatic activity, machine learning, Sanfilippo syndrome, variants of unknown significance},
doi = {10.1002/humu.23875},
url = {https://onlinelibrary.wiley.com/doi/abs/10.1002/humu.23875},
eprint = {https://onlinelibrary.wiley.com/doi/pdf/10.1002/humu.23875},
abstract = {Abstract The NAGLU challenge of the fourth edition of the Critical Assessment of Genome Interpretation experiment (CAGI4) in 2016, invited participants to predict the impact of variants of unknown significance (VUS) on the enzymatic activity of the lysosomal hydrolase α-N-acetylglucosaminidase (NAGLU). Deficiencies in NAGLU activity lead to a rare, monogenic, recessive lysosomal storage disorder, Sanfilippo syndrome type B (MPS type IIIB). This challenge attracted 17 submissions from 10 groups. We observed that top models were able to predict the impact of missense mutations on enzymatic activity with Pearson's correlation coefficients of up to 0.61. We also observed that top methods were significantly more correlated with each other than they were with observed enzymatic activity values, which we believe speaks to the importance of sequence conservation across the different methods. Improved functional predictions on the VUS will help population scale analysis of disease epidemiology and rare variant association analysis. This article is protected by copyright. All rights reserved.}
}
```
