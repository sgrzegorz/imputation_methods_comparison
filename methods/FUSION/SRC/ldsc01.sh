#!/bin/bash
. $(git rev-parse --show-toplevel)/definitions.config

# "conda activate ldsc"

file=$COMMON_INPUT/27989323-GCST004430-EFO_0008173.h.tsv

cd $FUSION/ldsc
python munge_sumstats.py  \
--sumstats $file \
--N 14          \
--snp hm_rsid \
--out $FUSION/OUTPUT/PGC2.SCZ

gzip -d $FUSION/OUTPUT/PGC2.SCZ.sumstats.gz

