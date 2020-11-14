# --------------------------- jak ja robilem ----------------------------------------------
conda create -n metaxcan python=3.5
conda install pip 
conda activate metaxcan
pip install h5py==2.8.0 numpy==1.15.4 pandas==0.23.4 patsy==0.5.1 pyarrow==0.9.0 pyliftover==0.3 rpy2 scipy==1.1.0 statsmodels==0.9.0
     
# https://github.com/hakyimlab/MetaXcan/wiki/Tutorial:-GTEx-v8-MASH-models-integration-with-a-Coronary-Artery-Disease-GWAS
# https://zenodo.org/record/3657902#.Xj2Zh-F7m90
#NALEŻY DOWNLOAD CAŁĄ ZAWARTOŚĆ [OK 16GB] I WYPAKOWAĆ FOLDER data DO FOLDERU ./software/DANE/data



#--------------------------- z readme ----------------------------------------------
#Download the code
git clone git@github.com:hakyimlab/summary-gwas-imputation.git
git clone git@github.com:hakyimlab/MetaXcan.git

# At the HPC cluster available to me, I load conda this way module load gcc/6.2.0 miniconda2/4.4.10
conda create -n metaxcan python=3.6
source activate metaxcan
conda install scipy numpy pandas -y
conda install -c conda-forge pyarrow -y
conda install -c bioconda pyliftover -y

wget  https://zenodo.org/record/3657902/files/sample_data.tar?download=1
tar -xvpf sample_data.tar\?download\=1
rm sample_data.tar\?download\=1
