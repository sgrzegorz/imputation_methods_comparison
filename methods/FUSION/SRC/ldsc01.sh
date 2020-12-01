#!/bin/bash
. $(git rev-parse --show-toplevel)/definitions.config

# przed uruchomieniem zrob conda activate ldsc (zainstaluj potrzebne biblioteki pod ta nazwa
# potem conda deactivate
file=/home/x/DEVELOPER1/WORK/inzynierka/DATA/GWAS/27989323-GCST004430-EFO_0008173.h.tsv



cd $FUSION/ldsc
python munge_sumstats.py  \
--sumstats $file \
--N 14          \
--snp hm_rsid \
--out $FUSION/OUTPUT/PGC2.SCZ

gzip -d $FUSION/OUTPUT/PGC2.SCZ.sumstats.gz

