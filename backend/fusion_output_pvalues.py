import csv
import math

import pandas as pd
import re
from definitions import ROOT_DIR


def fusion_output_pvalues(before,after,output):
    columns = ["gene","min_pvalue"]
    dtypes ={"gene": str,"min_pvalue":float}
    before = pd.read_csv(before, usecols=columns,dtype=dtypes,sep='\t',header=(0))

    columns = ['ID','MODELCV.PV']
    dtypes ={"ID": str,"MODELCV.PV":float}
    after = pd.read_csv(after, usecols=columns,dtype=dtypes,sep='\t',header=(0))

    after['before_pvalue'] = [-1.0 for i in after.ID]


    for index, (gene,min_pvalue) in before.iterrows():
        for id in after.ID:  # TOP3B'
            if id == gene:
                # after['before_pvalue'] =
                after.loc[after.ID == id, 'before_pvalue'] = min_pvalue
        pass
        if index%1000==0:
            print(f'{index}/{len(before)}')


    with open(output, 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(("gene", "before","after"))
        for index, row in after.iterrows():
            try:
                if row['before_pvalue'] == -1:
                    print(f'gene {row["ID"]} was not found in before pvalues')
                else:
                    writer.writerow((row['ID'] ,row['before_pvalue'],row['MODELCV.PV']))
            except KeyError as e:
                print(e)

    print('Finished, all other saved to file')


if __name__ == '__main__':
    before=f'{ROOT_DIR}/output/pvalues_input.csv'
    after =f'{ROOT_DIR}/methods/FUSION/OUTPUT/PGC2.SCZ.22.dat'
    output=f'{ROOT_DIR}/output/fusion_before_after.csv'
    fusion_output_pvalues(before, after,output)