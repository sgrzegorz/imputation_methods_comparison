# Predixcan

./PrediXcan.py --predict --assoc --linear \
               --weights weights/TW_Cells_EBV-transformed_lymphocytes_0.5.db \
               --dosages genotype \
               --samples samples.txt \
               --pheno phenotype/igrowth.txt \
               --output_prefix results/Cells_EBV-transformed_lymphocytes 

# Metaxcan
cd Metaxcan/software
GWAS_TOOLS=/home/x/DEVELOPER1/WORK/inzynierka/imputation_methods_comparison/methods/MetaXcan/software/genomic_tools/src
METAXCAN=/home/x/DEVELOPER1/WORK/inzynierka/imputation_methods_comparison/methods/MetaXcan/software
DATA=
OUTPUT=

./MetaXcan.py \
--model_db_path data/DGN-WB_0.5.db \
--covariance data/covariance.DGN-WB_0.5.txt.gz \
--gwas_folder data/GWAS \
--gwas_file_pattern ".*gz" \
--snp_column SNP \
--effect_allele_column A1 \
--non_effect_allele_column A2 \
--beta_column BETA \
--pvalue_column P \
--output_file results/test.csv

# Fusion

http://gusevlab.org/projects/fusion/
R
install.packages('Rcpp')
sudo apt-get install r-cran-rcppeigen


Rscript FUSION.assoc_test.R --sumstats PGC2.SCZ.sumstats --weights ./WEIGHTS/GTEx.Whole_Blood.pos --weights_dir ./WEIGHTS/ --ref_ld_chr ./LDREF/1000G.EUR. --chr 22 --out PGC2.SCZ.22.dat



# Tigar
cd TIGAR
Gene_Exp_path=./example_data/Gene_Exp.txt
sampleID=./example_data/sampleID.txt
genofile=./example_data/Genotype/example.vcf.gz
out_prefix=./Result

./TIGAR_Model_Train.sh --model elastic_net --Gene_Exp ${Gene_Exp_path} --sampleID ${sampleID} --chr 1 --genofile_type vcf --genofile ${genofile} --Format GT --out ${out_prefix}

./TIGAR_Model_Train.sh --model DPR --Gene_Exp ${Gene_Exp_path} --sampleID ${sampleID} --chr 1 --genofile_type vcf --genofile ${genofile} --Format GT --out ${out_prefix}


#### ======================================================================
genofile=./example_data/Genotype/example.vcf.gz
sampleID=./example_data/sampleID.txt
out_prefix=./Result
##### --------------------------------------

train_weight_path=./Result/elastic_net_CHR1/CHR1_elastic_net_training_weight.txt
train_info_path=./Result/elastic_net_CHR1/CHR1_elastic_net_training_info.txt
./TIGAR_Model_Pred.sh --model elastic_net --chr 1 --train_weight_path ${train_weight_path} --train_info_path ${train_info_path} --genofile_type vcf --genofile ${genofile} --sampleID ${sampleID} --Format GT --out ${out_prefix}

##### --------------------------------------

train_weight_path=./Result/DPR_CHR1/CHR!_DPR_training_weight.txt
train_info_path=./Result/DPR_CHR1/CHR1_DPR_training_info.txt
./TIGAR_Model_Pred.sh --model DPR --chr 1 --train_weight_path ${train_weight_path} --train_info_path ${train_info_path} --genofile_type vcf --genofile ${genofile} --sampleID ${sampleID} --Format GT --out ${out_prefix}
