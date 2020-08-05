# Predixcan

# Metaxcan


# Fusion

http://gusevlab.org/projects/fusion/

`R`

Rscript ../FUSION.assoc_test.R --sumstats PGC2.SCZ.sumstats --weights ./WEIGHTS/GTEx.Whole_Blood.pos --weights_dir ./WEIGHTS/ --ref_ld_chr ./LDREF/1000G.EUR. --chr 22 --out PGC2.SCZ.22.dat



# Tigar
cd TIGAR
genofile=./example_data/Genotype/example.vcf.gz
sampleID=./example_data/sampleID.txt
train_weight_path=./Result/elastic_net_CHR1/CHR1_elastic_net_training_weight.txt
train_info_path=./Result/elastic_net_CHR1/CHR1_elastic_net_training_info.txt
out_prefix=./Result
./TIGAR_Model_Pred.sh --model elastic_net --chr 1 --train_weight_path ${train_weight_path} --train_info_path ${train_info_path} --genofile_type vcf --genofile ${genofile} --Format GT --out ${out_prefix}
