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

The installation was tested on Ubuntu18.04

Download this repository from github, then:

#### conda environments

Open the project directory *imputation_methods_comparison* in the terminal and execute the following commands:

```
cd conda_env
conda env create -f main.yml
conda env create -f metaxcan.yml
conda env create -f tigar.yml
```

Optional conda installation commands, not necessary for a basic usage:
```
conda env create -f ldsc
conda env create -f second
```

#### R environment (for Fusion only)

The installation process for R environment is identical as provided by authors of Fusion software [More information about installation](http://gusevlab.org/projects/fusion/)

###### Plink library
At the beginning download and unpack the plink library

```
wget https://github.com/gabraham/plink2R/archive/master.zip
unzip master.zip
```

Plink library has two dependencies. On Ubuntu18.04 we installed them with the following commands:

- `sudo apt-get install r-cran-rcppeigen`   alternatively try: ` install.packages(c('RcppEigen', 'digest'))`
- Type `R` and paste:`install.packages('Rcpp')`

Type `R` in and install plink `install.packages('plink2R-master/plink2R/',repos=NULL)`

###### Other dependencies
Type `R` and install:
```
install.packages(c('optparse','RColorBrewer'))
install.packages(c('glmnet','methods'))
```
#### Tigar dependencies

Install [tabix](http://www.htslib.org/doc/tabix.html ) and [bgzip](http://www.htslib.org/doc/bgzip.html). We used the following command:

```
sudo apt-get install -y tabix
```

#### Project dependencies
Open file *imputation_methods_comparison/definitions.py*. Update CONDA variable in this file, if a path to *conda.sh* file in your system is different.



## Run

Open project directory `imputation_methods_comparison` in the terminal and type:
```
conda activate main
python main.py
```


## FAQ installation and usage (Ubuntu18.04)

- To complete installing conda environments, you may need to run  `sudo apt-get install gcc python3-dev`
 - `python main.py` does not start, because of [QT5 problem](https://askubuntu.com/questions/308128/failed-to-load-platform-plugin-xcb-while-launching-qt5-app-on-linux-without) . Try: `sudo apt-get install --reinstall libxcb-xinerama0`
 - When you run an imputation method and see *LINE 19: 123456 Killed* check system logs in */var/log/syslog*. Probably you have too little RAM on your machine and kernel stops the bash script. A solution for this issue could be creating a [swap file](https://help.ubuntu.com/community/SwapFaq)

