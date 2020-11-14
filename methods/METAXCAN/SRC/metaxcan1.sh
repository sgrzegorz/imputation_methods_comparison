#!/bin/bash

cd ..
input=./INPUT/sample_data/data

./software/SPrediXcan.py \
--model_db_path ${input}/DGN-WB_0.5.db \
--covariance ${input}/covariance.DGN-WB_0.5.txt.gz \
--gwas_folder ${input}/GWAS \
--gwas_file_pattern ".*gz" \
--snp_column SNP \
--effect_allele_column A1 \
--non_effect_allele_column A2 \
--beta_column BETA \
--pvalue_column P \
--output_file ./OUTPUT/test.csv

