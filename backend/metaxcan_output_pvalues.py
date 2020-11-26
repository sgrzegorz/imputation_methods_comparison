import csv
import math
import pandas as pd
import re
from definitions import ROOT_DIR

def metaxcan_output_pvalues(before,after,output):
    columns = ["gene","min_pvalue"]
    dtypes ={"gene": str,"min_pvalue":float}
    before = pd.read_csv(before, usecols=columns,dtype=dtypes,sep='\t',header=(0))

    columns = ['gene_name','pvalue']
    dtypes ={"gene_name": str,"pvalue":float}

    after = pd.read_csv(after, usecols=columns,dtype=dtypes,sep=',',header=(0))

    after['before_pvalue'] = [-1.0 for i in after.gene_name]


    for index, (gene,min_pvalue) in before.iterrows():
        for id in after.gene_name:  # TOP3B'
            if id == gene:      #TODO: co jak ten if zachodzi kilkukrotnie dla jednego id?
                # after['before_pvalue'] =
                after.loc[after.gene_name == id, 'before_pvalue'] = min_pvalue
        pass
        if index%1000==0:
            print(f'{index}/{len(before)}')


    with open(output, 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(("gene", "before","after"))
        for index, row in after.iterrows():
            try:
                if row['before_pvalue'] == -1:
                    print(f'gene {row["gene_name"]} was not found in before pvalues')
                else:
                    writer.writerow((row['gene_name'] ,row['before_pvalue'],row['pvalue']))
            except KeyError as e:
                print(e)

    print('Finished, all other saved to file')

if __name__ =='__main__':
    before=f'{ROOT_DIR}/output/pvalues_input.csv'
    after=f'{ROOT_DIR}/methods/METAXCAN/OUTPUT/spredixcan/eqtl/CARDIoGRAM_C4D_CAD_ADDITIVE__PM__Whole_Blood.csv'
    output=f'{ROOT_DIR}/output/metaxcan_before_after.csv'
    metaxcan_output_pvalues(before, after, output)