print('Hello World')
import os

PREDIX_PATH = 'methods/PrediXcanExample'

predixcan_command =  f'cd {PREDIX_PATH} && python3 PrediXcan.py --predict --assoc --linear  --weights weights/TW_Cells_EBV-transformed_lymphocytes_0.5.db    --dosages genotype       --samples samples.txt       --pheno phenotype/igrowth.txt       --output_prefix results/Cells_EBV-transformed_lymphocytes '
os.system(predixcan_command)

