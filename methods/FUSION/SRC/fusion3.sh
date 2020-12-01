#!/bin/bash

cd ..

input=./INPUT/input1
output=./OUTPUT


cat ${output}/PGC2.SCZ.22.dat | awk 'NR == 1 || $NF < 0.05/2058' > ${output}/PGC2.SCZ.22.top

Rscript FUSION.post_process.R \
--sumstats ${input}/PGC2.SCZ.sumstats \
--input ${output}/PGC2.SCZ.22.top \
--out ${output}/PGC2.SCZ.22.top.analysis \
--ref_ld_chr ./LDREF/1000G.EUR. \
--chr 22 \
--plot_corr	\
--report \
--plot \
--locus_win 100000 \
--plot_legend joint
