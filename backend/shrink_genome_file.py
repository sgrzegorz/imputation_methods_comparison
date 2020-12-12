import csv

import vcfpy
from definitions import ROOT_DIR

reader = vcfpy.Reader.from_path('../methods/00-common_all.vcf')

genes = []
rs = []

for i,record in enumerate(reader): 
    try:
        gene_infos = record.INFO['GENEINFO']
    except KeyError:
        continue
    gene_infos = gene_infos.split("|")
    gene_names = list(map(lambda x: (x.split(':'))[0], gene_infos))
    for gene_name in gene_names:
        genes.append(gene_name)
        rs.append(record.ID[0])

    if i%3000000==0:
        print(f'{i/37303035*100}%') 
print('Sort two arrays together')
zipped_lists = zip(genes, rs)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
genes, rs = [ list(tuple) for tuple in  tuples]


with open(f'{ROOT_DIR}/methods/gene_snp_mapping1.csvfile', 'w+') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(("gene", "snp"))
    for i in range(len(genes)):
        writer.writerow((genes[i] ,rs[i]))

