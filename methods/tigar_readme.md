//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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
