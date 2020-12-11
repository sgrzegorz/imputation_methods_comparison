#!/bin/bash

cd ..

# input=
output=./OUTPUT

./PrediXcan.py --predict --assoc --linear \
               --weights weights/TW_Cells_EBV-transformed_lymphocytes_0.5.db \
               --dosages genotype \
               --samples samples.txt \
               --pheno phenotype/igrowth.txt \
               --output_prefix ${output}/Cells_EBV-transformed_lymphocytes
               


