#!/bin/bash
# skrypt ktory wywoluje TIGAR na defaultowych ustawieniach bazuje na https://github.com/sgrzegorz/TIGAR/blob/master/TIGAR_Manual.pdf
# chmod a+x <skrypt.sh> ###jak <skrypt .sh> nie chce sie odpalic

cd TIGAR

##################################################### cis-eQTL Effect-Sizes Calculation ################################################################
echo cis-eQTL Effect-Sizes Calculation

Gene_Exp_path=./example_data/Gene_Exp.txt
sampleID=./example_data/sampleID.txt
genofile=./example_data/Genotype/example.vcf.gz
out_prefix=./Result

# ---------------------- Elastic-Net Regression ---------------------------------
echo Elastic-Net Regression

./TIGAR_Model_Train.sh --model elastic_net \
--Gene_Exp ${Gene_Exp_path} --sampleID ${sampleID} \
--chr 1 --genofile_type vcf \
--genofile ${genofile} --Format GT \
--out ${out_prefix}

# ---------------------- DPR ---------------------------------
echo DPR

./TIGAR_Model_Train.sh --model DPR \
--Gene_Exp ${Gene_Exp_path} --sampleID ${sampleID} \
--chr 1 --genofile_type vcf \
--genofile ${genofile} --Format GT \
--out ${out_prefix}


############################################################# 3 GReX Prediction ##########################################################################
echo 3 GReX Prediction

genofile=./example_data/Genotype/example.vcf.gz
sampleID=./example_data/sampleID.txt
out_prefix=./Result

# ---------------------- Elastic-Net Regression Based---------------------------------
echo Elastic-Net Regression Based

train_weight_path=./Result/elastic_net_CHR1/CHR1_elastic_net_training_weight.txt
train_info_path=./Result/elastic_net_CHR1/CHR1_elastic_net_training_info.txt

./TIGAR_Model_Pred.sh --model elastic_net \
--chr 1 \
--train_weight_path ${train_weight_path} \
--train_info_path ${train_info_path} \
--genofile_type vcf \
--genofile ${genofile} \
--sampleID ${sampleID} \
--Format GT \
--out ${out_prefix}

# --------------------------------- DPR Based---------------------------------
echo DPR Based

train_weight_path=./Result/DPR_CHR1/CHR1_DPR_training_weight.txt
train_info_path=./Result/DPR_CHR1/CHR1_DPR_training_info.txt

./TIGAR_Model_Pred.sh --model DPR \
--chr 1 \
--train_weight_path ${train_weight_path} \
--train_info_path ${train_info_path} \
--genofile_type vcf \
--genofile ${genofile} \
--sampleID ${sampleID} \
--Format GT \
--out ${out_prefix}

################################################################ 4 TWAS ##################################################################################
# ------------ Type One Association Study ----------------------------
echo Type One Association Study

Gene_Exp_path=./Result/DPR_CHR1/CHR1_DPR_GReX_prediction.txt
PED=./example_data/example_PED.ped
Asso_Info=./example_data/Asso_Info/Asso_Info_SinglePheno_OLS.txt
out_prefix=./Result/DPR_CHR1

./TIGAR_TWAS.sh --asso 1 \
--Gene_Exp ${Gene_Exp_path} \
--PED ${PED} --Asso_Info ${Asso_Info} \
--out ${out_prefix}


#------------ Type Two Association Study -----------------------------------
echo Type Two Association Study

Gene_Exp_path=./example_data/Gene_Exp.txt
Zscore=./example_data/example_Zscore/CHR1_GWAS_Zscore.txt.gz
Weight=./Result/DPR_CHR1/CHR1_DPR_training_weight.txt
Covar=./Result/reference_cov/CHR1_reference_cov.txt.gz
out_prefix=./Result/DPR_CHR1

./TIGAR_TWAS.sh --asso 2 \
--Gene_Exp ${Gene_Exp_path} \
--Zscore ${Zscore} --Weight ${Weight} --Covar ${Covar} --chr 1 \
--out ${out_prefix}



####################################################### Generate Reference Covariance File ##########################################################
echo Generate Reference Covariance File

block=./example_data/block_annotation_EUR.txt
genofile=./example_data/Genotype/example.vcf.gz
out_prefix=./Result

./TWAS/Covar/TIGAR_Covar.sh --block ${block} \
--genofile_type vcf --genofile ${genofile} \
--chr 1 \
--Format GT \
--out ${out_prefix}


