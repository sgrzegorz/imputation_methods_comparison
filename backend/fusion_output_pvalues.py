import csv
import math

import pandas as pd
import re


columns = ["gene","min_pvalue"]
dtypes ={"gene": str,"min_pvalue":float}
before = pd.read_csv('pictures/input_wyniki.csv', usecols=columns,dtype=dtypes,sep='\t',header=(0))

columns = ['ID','MODELCV.PV']
dtypes ={"ID": str,"MODELCV.PV":float}
after = pd.read_csv('../methods/fusion_twas-master/OUTPUT/PGC2.SCZ.22.dat', usecols=columns,dtype=dtypes,sep='\t',header=(0))

after['before_pvalue'] = [-1.0 for i in after.ID]


for index, row in before.iterrows():
    for id in after.ID:  # TOP3B'
        if id in row['gene']:    #TODO: co jak ten if zachodzi kilkukrotnie dla jednego id?
            # after['before_pvalue'] =
            after.loc[after.ID == id, 'before_pvalue'] = row['min_pvalue']
    pass
    if index%1000==0:
        print(f'{index}/{len(before)}')


with open('pictures/fusion_before_after.csv', 'w+') as csvfile:
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
