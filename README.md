# Imputation Methods Comparison

The idea of our project is  to create a platform a platform for comparison of imputation methods of gene expression. 
Currently we support an user friendly GUI interface for the following imputation methods:

- [MetaXcan](https://github.com/hakyimlab/MetaXcan)
- [Fusion](http://gusevlab.org/projects/fusion)
- [Tigar](https://github.com/xmeng34/TIGAR)

## Demo

<img src='docs/movie.gif' align="center" width=784>
<br><br><br>


## Installation

#### conda environments

Open the project directory `imputation_methods_comparison` in the terminal and execute the following commands:

```
cd conda_env
conda env create -f main.yml
conda env create -f metaxcan.yml
conda env create -f tigar.yml
conda env create -f ldsc
conda env create -f second
```

#### R environment (for Fusion only)

The installation process is identical as provided by authors of Fusion software [More information about installation](http://gusevlab.org/projects/fusion/)

At the beginning download and unpack the plink library

```
wget https://github.com/gabraham/plink2R/archive/master.zip
unzip master.zip
```

Type `R` in terminal. And install required libraries: 

```
install.packages('plink2R-master/plink2R/',repos=NULL)
install.packages(c('optparse','RColorBrewer'))
install.packages(c('glmnet','methods'))

```

