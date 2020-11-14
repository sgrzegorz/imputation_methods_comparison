#!/bin/bash

cd ..

GWAS_TOOLS=./GWAS_TOOLS
METAXCAN=./software
input=./INPUT/input1
output=./OUTPUT

# ---------------------------------------------------------------------------------------------
# harmonize input gWAS to our reference
echo harmonize input gWAS to our reference

# output_column_map effect_allele effect_allele tutaj nie uzylem hm_effect_allele bo program sie gubil i widzial dwie kolumny effect_allele
python $GWAS_TOOLS/gwas_parsing.py \
-gwas_file /home/x/Downloads/GWAS2/27989323-GCST004430-EFO_0008173.h.tsv \
-liftover ${input}/liftover/hg19ToHg38.over.chain.gz \
-snp_reference_metadata ${input}/reference_panel_1000G/variant_metadata.txt.gz METADATA \
-output_column_map hm_other_allele non_effect_allele \
-output_column_map effect_allele effect_allele \
-output_column_map hm_beta effect_size \
-output_column_map p_value pvalue \
-output_column_map chromosome chromosome \
-output_column_map variant_id variant_id \
-output_column_map standard_error standard_error \
-output_column_map hm_pos position \
-output_column_map hm_effect_allele_frequency frequency \
--insert_value sample_size 9605470 --insert_value n_cases 9605470 \
--chromosome_format \
-verbosity 1 \
-output_order variant_id panel_variant_id chromosome position effect_allele non_effect_allele frequency pvalue zscore effect_size standard_error sample_size n_cases \
-output ${output}/harmonized_gwas/CARDIoGRAM_C4D_CAD_ADDITIVE.txt.gz

#-output_order variant_id chromosome position effect_allele non_effect_allele frequency pvalue effect_size standard_error \
#--insert_value sample_size 184305 --insert_value n_cases 60801 \
#-output_column_map hm_effect_allele effect_allele \
#-output_order variant_id panel_variant_id chromosome position effect_allele non_effect_allele frequency pvalue zscore effect_size standard_error sample_size n_cases \
