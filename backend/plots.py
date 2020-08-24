import os
import time

import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import codecs

METAXCAN_RESULTS_PATH = 'methods/MetaXcan/RESULTS/spredixcan/eqtl/CARDIoGRAM_C4D_CAD_ADDITIVE__PM__Whole_Blood.csv'
FUSION_RESULTS_PATH = 'methods/fusion_twas-master/PGC2.SCZ.22.dat'

def _save_picture(filename):
    if os.path.isfile(f'backend/pictures/{filename}.png'):
        os.remove(f'backend/pictures/{filename}.png')

    plt.savefig(f'backend/pictures/{filename}')

    # plt.show()
    plt.close()



def metaxcan0_pvalue_and_pred_perf_r2_plot():
    data = pd.read_csv(METAXCAN_RESULTS_PATH)
    data['pvalue'].plot(kind='line',color='brown')
    plt.title('metaxcan pvalue')
    plt.xlabel('gene number')
    plt.ylabel('pvalue')

    # if os.path.isfile('backend/pictures/metaxcan0.png'):
    #     os.remove('backend/pictures/metaxcan0.png')
    # plt.savefig('backend/pictures/metaxcan0')
    _save_picture('metaxcan0')
    # data['pred_perf_r2'].plot(color='red') TODO
    #plt.plot(data['pred_perf_r2'])
    # data.plot(y='pred_perf_r2',color='red')
    # plt.scatter(x=1:data.shape[0] ,y=data['pred_perf_r2'])
    # plt.title('metaxcan pred_perf_r2')
    # plt.xlabel('gene number')
    # plt.ylabel('pred_perf_r2')
    # plt.show()

def metaxcan1_pvalue_histogram_plot():
    data = pd.read_csv(METAXCAN_RESULTS_PATH)
    histogram = data['pvalue'].hist(bins=100)
    # pvalues are from 0 to 1
    plt.title('metaxcan pvalue histogram')
    plt.xlabel('bins')
    plt.ylabel('number of pvalue\'s')
    _save_picture('metaxcan1')


def metaxcan2_pvalue_best_gwas_p_difference_plot():
    data = pd.read_csv(METAXCAN_RESULTS_PATH)
    data1 = pd.DataFrame()
    data1['difference between pvalue and best_gwas_p'] = data['pvalue'] - data[
        'best_gwas_p']
    data1.plot()
    _save_picture('metaxcan2')


# powinien wyjsc rozklad normalny
def fusion0_best_gwas_z_plot(): #TODO ma niewlasciwy ksztalt
    data = pd.read_csv(FUSION_RESULTS_PATH, sep='\t', header=(0))
    data['BEST.GWAS.Z'].plot(kind='line')
    plt.title('fusion best gwas z plot')
    plt.xlabel('gene number')
    plt.ylabel('best gwas z')

    _save_picture('fusion0')



# ma ładnie spadać do wypłaszczonej krzywej
def fusion1_twas_p_plot(): #TODO Na raze nie chce spadać...
    data = pd.read_csv(FUSION_RESULTS_PATH, sep='\t', header=(0))
    data['TWAS.P'].plot(kind='line')
    plt.title('fusion twas p plot')
    plt.xlabel('gene number')
    plt.ylabel('twas p')
    _save_picture('fusion1')


def fusion2_lasso_vs_enet_diagram():
    data = pd.read_csv(FUSION_RESULTS_PATH, sep='\t', header=(0))

    labels = 'lasso', 'enet'
    occurrences = data['MODEL'].value_counts()
    number_lasso = occurrences['lasso']
    number_enet = occurrences['enet']
    sizes = [number_lasso, number_enet]
    fig1, ax1 = plt.subplots()
    explode = (0.05, 0.05) #wysuniencie polowek diagramu
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Fusion: lasso vs enet statistics')

    _save_picture('fusion2')


def fusion_metaxcan_compare_modelcvr2_predictive_performance_r2_plot(): #TODO
    metaxcan_data = pd.read_csv(METAXCAN_RESULTS_PATH)
    fusion_data = pd.read_csv(FUSION_RESULTS_PATH, sep='\t', header=(0))
    fusion_data['MODELCV.R2']
    print(metaxcan_data['pred_perf_r2'])

# function which prints full pandas dataframe without dots (...) very usefull. Eg print_full(dataframe) Używać zamiast print(dataframe)!
def print_full_fusion(x):
    pd.set_option('display.max_rows', len(x))
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')

# metaxcan_pvalue_and_pred_perf_r2_plot()

