#!/bin/bash

# setup
# http://gusevlab.org/projects/fusion/
# R
# install.packages('Rcpp')
# sudo apt-get install r-cran-rcppeigen


cd ..

input=./INPUT/input1
output=./OUTPUT

Rscript FUSION.assoc_test.R \
--sumstats ${output}/PGC2.SCZ.sumstats \
--weights ${input}/WEIGHTS/GTEx.Whole_Blood.pos \
--weights_dir ${input}/WEIGHTS/ \
--ref_ld_chr ./LDREF/1000G.EUR. \
--chr 22 \
--out ${output}/PGC2.SCZ.22.dat


