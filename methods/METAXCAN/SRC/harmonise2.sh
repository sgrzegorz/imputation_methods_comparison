#!/bin/bash

cd ..

GWAS_TOOLS=./GWAS_TOOLS
METAXCAN=./software
input=./INPUT/input1
output=./OUTPUT

# ---------------------------------------------------------------------------------------------
# harmonize input gWAS to our reference
echo harmonize input gWAS to our reference

#python $GWAS_TOOLS/gwas_parsing.py \
#-gwas_file /home/x/DEVELOPER1/WORK/inzynierka/DATA/GWAS/27989323-GCST004430-EFO_0008173.h.tsv \
#-output_column_map hm_variant_id variant_id \
#-output_column_map hm_other_allele non_effect_allele \
#-output_column_map hm_effect_allele effect_allele \
#-output_column_map hm_beta effect_size \
#-output_column_map p_value pvalue \
#-output_column_map hm_chrom chromosome \
#-output_column_map standard_error standard_error \
#-output_column_map hm_pos position \
#-output_column_map hm_effect_allele_frequency frequency \
#--insert_value sample_size 184305 --insert_value n_cases 60801 \
#-output_order variant_id panel_variant_id chromosome position effect_allele non_effect_allele frequency pvalue zscore effect_size standard_error sample_size n_cases \
#-output ${output}/harmonized_gwas/CARDIoGRAM_C4D_CAD_ADDITIVE.txt.gz


python $METAXCAN/M03_betas.py \
--snp_map_file ${input}/coordinate_map/map_snp150_hg19.txt.gz \
--gwas_file /home/x/DEVELOPER1/WORK/inzynierka/DATA/GWAS/27989323-GCST004430-EFO_0008173.h.tsv.gz \
--snp_column hm_variant_id \
--non_effect_allele_column hm_other_allele \
--effect_allele_column hm_effect_allele \
--pvalue_column p_value \
--beta_column hm_beta \
--se_column  standard_error \
--position_column hm_pos  \
--keep_non_rsid \
--throw \
--output ${output}/harmonized_gwas/CARDIoGRAM_C4D_CAD_ADDITIVE.txt.gz


#-output_order variant_id chromosome position effect_allele non_effect_allele frequency pvalue effect_size standard_error \
#
#--keep_non_rsid \
#
