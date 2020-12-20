#!/bin/bash

cd ..
input=./INPUT/predixcan_sample_data/data
output=./OUTPUT

python3 ./software/PrediXcan.py \
--model_db_path $input/models/gtex_v8_en/en_Whole_Blood.db \
--vcf_genotypes $input/1000G_hg37/ALL.chr*.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz \
--vcf_mode genotyped \
--prediction_output $output/vcf_1000G_hg37_en_b/Whole_Blood__predict.txt \
--prediction_summary_output $output/vcf_1000G_hg37_en_b/Whole_Blood__summary.txt \
--input_phenos_file $input/1000G_hg37/random_pheno_1000G_hg37.txt \
--input_phenos_column pheno \
--output $output/vcf_1000G_hg37_en_b/Whole_Blood__association.txt \
--verbosity 9 \
--throw