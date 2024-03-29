import csv
import math
import pandas as pd
from definitions import ROOT_DIR
import sys


def input_pvalues(GWAS_PATH,OUTPUT_PATH):

    print('Reading snps from input GWAS file')
    columns = ["hm_rsid","p_value"]
    dtypes ={'hm_rsid': str,'p_value':float}
    gwas = pd.read_csv(GWAS_PATH, usecols=columns, dtype=dtypes,sep='\t', header=(0))
    gwas.columns = ['rs', 'p_value']

    print('Converting snps from input GWAS file')
    gwas_rs = set(gwas.rs)
    gwas = dict(zip(gwas.rs, gwas.p_value))  

    def get_min_pvalue(gwas,current_gene,RS):
        min_pvalue = math.inf

        for rs in RS[current_gene]:
            try:
                candidate = gwas[rs]
                if candidate < min_pvalue:
                    min_pvalue = candidate
            except Exception as e:
                print(e)
        return min_pvalue


    print('Load gwas reference')
    g_reference = pd.read_csv(f'{ROOT_DIR}/methods/gene_snp_mapping.csvfile',sep='\t', header=(0))
    g_rows_count = g_reference.shape[0]


    print('Main loop starts')
    GENES = set() 
    RS = {} 
    MIN_PVALUES = {}
    GENES.add('INITIAL')
    RS['INITIAL']=set()
    len(g_reference)
    current_gene ='INITIAL'  
    for i, (g_gene,g_rs) in g_reference.iterrows():

        if current_gene !=g_gene: 
            RS[current_gene] = gwas_rs.intersection(RS[current_gene]) 

            if len(RS[current_gene]) ==0: 
                GENES.remove(current_gene)
                RS.pop(current_gene)
            else:
                MIN_PVALUES[current_gene] =get_min_pvalue(gwas, current_gene,RS)
            current_gene = g_gene

        GENES.add(g_gene)
        if g_gene in RS:
            RS[g_gene].add(g_rs)
        else:
            RS[g_gene] = set()
            RS[g_gene].add(g_rs)

        if i%3000000==0:
            print(f'{math.floor(i/g_rows_count*100)}%') 

    with open(OUTPUT_PATH, 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(("gene", "min_pvalue"))
        for gene_name in GENES:
            try:
                writer.writerow((gene_name ,MIN_PVALUES[gene_name]))
            except KeyError as e:
                print(e)

    print('Finished')


if __name__ =='__main__':

    GWAS_PATH = sys.argv[1]
    OUTPUT_PATH = sys.argv[2]
    input_pvalues(GWAS_PATH,OUTPUT_PATH)