#!/bin/bash
# run "metaxcan.sh" before this script

cd ..
input=./INPUT/input1
output=./OUTPUT

python ./software/SMulTiXcan.py \
--models_folder $input/models/eqtl/mashr \
--models_name_pattern "mashr_(.*).db" \
--snp_covariance $input/models/gtex_v8_expression_mashr_snp_smultixcan_covariance.txt.gz \
--metaxcan_folder $output/spredixcan/eqtl/ \
--metaxcan_filter "CARDIoGRAM_C4D_CAD_ADDITIVE__PM__(.*).csv" \
--metaxcan_file_name_parse_pattern "(.*)__PM__(.*).csv" \
--gwas_file $output/processed_summary_imputation_1000G/imputed_CARDIoGRAM_C4D_CAD_ADDITIVE.txt.gz \
--snp_column panel_variant_id \
--effect_allele_column effect_allele \
--non_effect_allele_column non_effect_allele \
--zscore_column zscore \
--keep_non_rsid \
--model_db_snp_key varID \
--cutoff_condition_number 30 \
--verbosity 7 \
--throw \
--output $output/smultixcan/eqtl/CARDIoGRAM_C4D_CAD_ADDITIVE_smultixcan.txt

