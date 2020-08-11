# Predixcan 

./PrediXcan.py --predict --assoc --linear \
               --weights weights/TW_Cells_EBV-transformed_lymphocytes_0.5.db \
               --dosages genotype \
               --samples samples.txt \
               --pheno phenotype/igrowth.txt \
               --output_prefix results/Cells_EBV-transformed_lymphocytes 
               

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Fusion

http://gusevlab.org/projects/fusion/
R
install.packages('Rcpp')
sudo apt-get install r-cran-rcppeigen


Rscript FUSION.assoc_test.R --sumstats PGC2.SCZ.sumstats --weights ./WEIGHTS/GTEx.Whole_Blood.pos --weights_dir ./WEIGHTS/ --ref_ld_chr ./LDREF/1000G.EUR. --chr 22 --out PGC2.SCZ.22.dat


