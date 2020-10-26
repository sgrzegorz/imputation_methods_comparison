#!/bin/bash

cd ..

GWAS_TOOLS=./GWAS_TOOLS
METAXCAN=./software
input=./INPUT/input1
output=./OUTPUT

# ---------------------------------------------------------------------------------------------
# harmonize input gWAS to our reference
echo harmonize input gWAS to our reference

python $GWAS_TOOLS/gwas_parsing.py \
-gwas_file /home/x/Downloads/GWAS2/27989323-GCST004430-EFO_0008173.h.tsv \
-output_column_map hm_variant_id variant_id \
-output_column_map hm_other_allele non_effect_allele \
-output_column_map hm_effect_allele effect_allele \
-output_column_map hm_beta effect_size \
-output_column_map p_value pvalue \
-output_column_map hm_chrom chromosome \
-output_column_map standard_error standard_error \
--chromosome_format \
-output_column_map hm_pos position \
-output_column_map hm_effect_allele_frequency frequency \
-output_order variant_id chromosome position effect_allele non_effect_allele frequency pvalue effect_size standard_error \
-output ${output}/harmonized_gwas/CARDIoGRAM_C4D_CAD_ADDITIVE.txt.gz

