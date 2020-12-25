#!/bin/bash
. $(git rev-parse --show-toplevel)/definitions.config
# ./test.sh | tee logs.txt

CONDA='/home/x/anaconda3/etc/profile.d/conda.sh'

source $CONDA

echo "##########################################################################################################################################################"
echo "##METAXCAN#################################################################################################################################################"
echo "##########################################################################################################################################################"
cd $METAXCAN/SRC
conda activate metaxcan


echo "////////////////////////////////////harmonise.sh//////////////////////////////////////////////////////////////////////////////////"
./harmonise.sh
echo "////////////////////////////////////harmonise1.sh//////////////////////////////////////////////////////////////////////////////////"
./harmonise1.sh
mkdir $METAXCAN/OUTPUT_HARMONISE
mv  -v $METAXCAN/OUTPUT/* $METAXCAN/OUTPUT_HARMONISE


echo "////////////////////////////////////metaxcan.sh//////////////////////////////////////////////////////////////////////////////////"
./metaxcan.sh
echo "////////////////////////////////////smultixcan.sh//////////////////////////////////////////////////////////////////////////////////"
./smultixcan.sh
mkdir $METAXCAN/OUTPUT_METAXCAN
mv  -v $METAXCAN/OUTPUT/* $METAXCAN/OUTPUT_METAXCAN


echo "////////////////////////////////////predixcan.sh//////////////////////////////////////////////////////////////////////////////////"
./predixcan.sh





echo "##########################################################################################################################################################"
echo "##FUSION#################################################################################################################################################"
echo "##########################################################################################################################################################"
cd $FUSION/SRC


echo "////////////////////////////////////ldsc01.sh//////////////////////////////////////////////////////////////////////////////////"
conda activate ldsc
./ldsc01.sh
echo "////////////////////////////////////fusion.sh ldsc data//////////////////////////////////////////////////////////////////////////////////"
./fusion.sh
echo "////////////////////////////////////fusion3.sh ldsc data//////////////////////////////////////////////////////////////////////////////////"
./fusion3.sh
mkdir $FUSION/OUTPUT_LDSC_VERSION
mv  -v $FUSION/OUTPUT/* $FUSION/OUTPUT_LDSC_VERSION


echo "////////////////////////////////////fusion again but with default data//////////////////////////////////////////////////////////////////////////////////"
cp $FUSION/INPUT/input1/PGC2.SCZ.sumstats $FUSION/OUTPUT
echo "////////////////////////////////////fusion.sh//////////////////////////////////////////////////////////////////////////////////"
./fusion.sh
echo "////////////////////////////////////fusion3.sh//////////////////////////////////////////////////////////////////////////////////"
./fusion3.sh




echo "##########################################################################################################################################################"
echo "##TIGAR#################################################################################################################################################"
echo "##########################################################################################################################################################"
cd $TIGAR/SRC
echo "////////////////////////////////////tigar.sh//////////////////////////////////////////////////////////////////////////////////"
conda activate tigar
./tigar.sh

echo "###################################################################################################################################################"