import csv
import os
import math
import vcfpy
import pandas as pd

# from configparser import ConfigParser
# config_object = ConfigParser()
# config_object.read("global.config")
# path =config_object["PATH"]
def achieve_min_pvalue(data,gene_name,rsy):
    min_val = math.inf

    for rs in rsy[gene_name]:
        try:
            candidate = data[rs]
            if candidate < min_val:
                min_val = candidate
        except Exception as e:
            print(e)
    return min_val



print('Reading snps')
columns = ["hm_rsid","p_value"]
dtypes ={'hm_rsid': str,'p_value':float}
data = pd.read_csv('/home/x/Downloads/GWAS2/27989323-GCST004430-EFO_0008173.h.tsv', usecols=columns,dtype=dtypes,sep='\t', header=(0))
# data = pd.read_csv('fusion01_wyniki.sumstats.gz',compression='gzip', sep='\t', header=(0))
# data = data.sort_values('hm_rsid')

print('Converting')
dataSNP = set(data.hm_rsid)
data = dict(zip(data.hm_rsid, data.p_value))  # dictionary get() has complexity O(1)


print('Starts loop')
genes = set()  # nazwy_genów
rsy = {} # rsy przyporządkowane każdemu genowi rs['nazwa_genu] = { zbiór wszystkich rsów przyporządkowanych danemu genowi
min_pvalues = {}


reader = vcfpy.Reader.from_path('../methods/00-common_all.vcf')
genes.add('INITIAL')
rsy['INITIAL']=set()
current_gene_name ='INITIAL'  # nazwa poprzedniego genu
for i,record in enumerate(reader): #iteruj po wierszach vcf-a
    try:
        gene_name = record.INFO['GENEINFO']
    except KeyError:
        continue

    if current_gene_name !=gene_name: # zmienil sie gen
        rsy[current_gene_name] = dataSNP.intersection(rsy[current_gene_name]) # wez przeciecie rs-ow

        if len(rsy[current_gene_name]) ==0: # jesli przeciecie jest puste gen nas nie interesuje wiec zapomnij go
            genes.remove(current_gene_name)
            rsy.pop(current_gene_name)
        else:
            min_pvalues[current_gene_name] =achieve_min_pvalue(data, current_gene_name,rsy)
        current_gene_name = gene_name

    # iterujac po wierszach vcf-a dodawaj kazdej nazwie genu jego rs-y
    snp = record.ID[0]
    genes.add(gene_name)
    if gene_name in rsy:
        rsy[gene_name].add(snp)
    else:
        rsy[gene_name] = set()
        rsy[gene_name].add(snp)

    if i%3000000==0:
        print(f'{i/37303035*100}%') # print progress in percents


with open('pictures/input_wyniki.csv', 'w+') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(("gene", "min_pvalue"))
    for gene_name in genes:
        try:
            writer.writerow((gene_name ,min_pvalues[gene_name]))
        except KeyError as e:
            print(e)

print('Finished')
