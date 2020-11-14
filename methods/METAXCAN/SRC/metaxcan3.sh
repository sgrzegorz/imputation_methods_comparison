#!/bin/bash

cd ..
input=./INPUT/input3

./software/SPrediXcan.py \
--model_db_path ${input}/DGN-WB_0.5.db \
--covariance ${input}/covariance.DGN-WB_0.5.txt.gz \
--gwas_file ${input}/LBD.GWAS.Summary.Stats.EBI.submission.formatted.tsv \
--snp_column variant_id \
--effect_allele_column effect_allele \
--non_effect_allele_column other_allele \
--beta_column beta \
--pvalue_column p_value \
--output_file ./OUTPUT/test.csv

