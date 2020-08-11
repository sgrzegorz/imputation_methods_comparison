# Metaxcan 
conda create -n metaxcan python=3.5
conda install pip 
conda activate metaxcan
pip install h5py==2.8.0 numpy==1.15.4 pandas==0.23.4 patsy==0.5.1 pyarrow==0.9.0 pyliftover==0.3 rpy2 scipy==1.1.0 statsmodels==0.9.0
     
https://github.com/hakyimlab/MetaXcan/wiki/Tutorial:-GTEx-v8-MASH-models-integration-with-a-Coronary-Artery-Disease-GWAS

https://zenodo.org/record/3657902#.Xj2Zh-F7m90
NALEŻY DOWNLOAD CAŁĄ ZAWARTOŚĆ [OK 16GB] I WYPAKOWAĆ DO FOLDERU ./software/DANE/data

cd Metaxcan
GWAS_TOOLS=./software/GWAS_TOOLS
METAXCAN=./software
DATA=./software/DANE/data
OUTPUT=RESULTS


# harmonize input gWAS to our reference
python $GWAS_TOOLS/gwas_parsing.py \
-gwas_file $DATA/gwas/cad.add.160614.website.txt.gz \
-liftover $DATA/liftover/hg19ToHg38.over.chain.gz \
-snp_reference_metadata $DATA/reference_panel_1000G/variant_metadata.txt.gz METADATA \
-output_column_map markername variant_id \
-output_column_map noneffect_allele non_effect_allele \
-output_column_map effect_allele effect_allele \
-output_column_map beta effect_size \
-output_column_map p_dgc pvalue \
-output_column_map chr chromosome \
--chromosome_format \
-output_column_map bp_hg19 position \
-output_column_map effect_allele_freq frequency \
--insert_value sample_size 184305 --insert_value n_cases 60801 \
-output_order variant_id panel_variant_id chromosome position effect_allele non_effect_allele frequency pvalue zscore effect_size standard_error sample_size n_cases \
-output $OUTPUT/harmonized_gwas/CARDIoGRAM_C4D_CAD_ADDITIVE.txt.gz

# The following imputes a portion of the imput GWAS.
# The imputation is meant to be split over many executions to improve paralellism
# so you would have to iterate `-chromosome` between [1,22] and `-sub_batch` between [0,_sub_batches],
# ideally in an HPVC environment ZADZIAŁAŁO Z CONDA METAXCAN
python $GWAS_TOOLS/gwas_summary_imputation.py \
-by_region_file $DATA/eur_ld.bed.gz \
-gwas_file $OUTPUT/harmonized_gwas/CARDIoGRAM_C4D_CAD_ADDITIVE.txt.gz \
-parquet_genotype $DATA/reference_panel_1000G/chr1.variants.parquet \
-parquet_genotype_metadata $DATA/reference_panel_1000G/variant_metadata.parquet \
-window 100000 \
-parsimony 7 \
-chromosome 1 \
-regularization 0.1 \
-frequency_filter 0.01 \
-sub_batches 10 \
-sub_batch 0 \
--standardise_dosages \
-output $OUTPUT/summary_imputation_1000G/CARDIoGRAM_C4D_CAD_ADDITIVE_chr1_sb0_reg0.1_ff0.01_by_region.txt.gz

# Finally, postprocess the harmonized input GWAs and all of the imputation batches' results
python $GWAS_TOOLS/gwas_summary_imputation_postprocess.py \
-gwas_file $OUTPUT/harmonized_gwas/CARDIoGRAM_C4D_CAD_ADDITIVE.txt.gz \
-folder $OUTPUT/summary_imputation_1000G \
-pattern "CARDIoGRAM_C4D_CAD_ADDITIVE.*" \
-parsimony 7 \
-output $OUTPUT/processed_summary_imputation_1000G/imputed_CARDIoGRAM_C4D_CAD_ADDITIVE.txt.gz

python $METAXCAN/SPrediXcan.py \
--gwas_file  $OUTPUT/processed_summary_imputation_1000G/imputed_CARDIoGRAM_C4D_CAD_ADDITIVE.txt.gz \
--snp_column panel_variant_id --effect_allele_column effect_allele --non_effect_allele_column non_effect_allele --zscore_column zscore \
--model_db_path $DATA/models/eqtl/mashr/mashr_Whole_Blood.db \
--covariance $DATA/models/eqtl/mashr/mashr_Whole_Blood.txt.gz \
--keep_non_rsid --additional_output --model_db_snp_key varID \
--throw \
--output_file $OUTPUT/spredixcan/eqtl/CARDIoGRAM_C4D_CAD_ADDITIVE__PM__Whole_Blood.csv



