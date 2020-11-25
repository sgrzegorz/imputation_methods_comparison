import csv
import datetime
import errno
import os,subprocess,sys
import resource
import time
import psutil
import pandas as pd
import matplotlib.pyplot as plt
import traceback
from definitions import ROOT_DIR

from threading import Thread
from time import sleep
import threading
lock = threading.Lock()

def _bytes_to_megabytes(bytes):
    return bytes/1000000


def getOutputPath(method_name):
    timestamp = str(time.strftime("%Y-%m-%d_%H-%M-%S"))
    return f'{ROOT_DIR}/output/resources/{method_name}{timestamp}.csv'


def _stats_with_children(process,writer):
    try:
        # obciazenie ram w bajtach
        rss = process.memory_full_info().rss
        swap = process.memory_full_info().swap
        # obciazenie rdzenia cpu w procentach jak wiecej niz 100% to pracuje na wiecej niz 1 rdzeniu
        cpu =process.cpu_percent(interval=0.1)

        user  =process.cpu_times().user
        system = process.cpu_times().system

        read_bytes = process.io_counters().read_bytes
        write_bytes = process.io_counters().write_bytes

        now = time.strftime("%m/%d/%Y, %H:%M:%S")

        for child in process.children(recursive=True):
            rss += child.memory_full_info().rss
            swap += child.memory_full_info().swap
            cpu+=child.cpu_percent(interval=0.1)
            user += child.cpu_times().user
            system += child.cpu_times().system

            read_bytes += child.io_counters().read_bytes
            write_bytes += child.io_counters().write_bytes

    except psutil.NoSuchProcess as e: # jedno z dzieci nagle przestalo byc zywe
        # print(traceback.format_exc())
        print('Dont worry :) -one of obeserved imputation method subprocesses disappeard')
        # print(type =type(e).__name__)


    rss =_bytes_to_megabytes(rss)
    swap=_bytes_to_megabytes(swap)
    read =_bytes_to_megabytes(read_bytes)
    write=_bytes_to_megabytes(write_bytes)
    writer.writerow((now,rss,swap,cpu,read,write))


def observe_process(pid,FILE):
    print(FILE)
    with open(FILE, 'w+') as file:
        writer = csv.writer(file, delimiter='\t')
        try:
            writer.writerow(("time", "rss",'swap','cpu','read','write'))
            while(psutil.pid_exists(pid)):
                process = psutil.Process(pid=pid)
                _stats_with_children(process,writer)

                sleep(1)
        except psutil.AccessDenied as e:
            type1 =type(e).__name__
            print(f'Dont worry :) Imputation process is finished so observer failed to find it and throwed {type1} error')
            # print(traceback.format_exc())

def observe_imputation_process(pid,method_name):
    FILE = getOutputPath(method_name)
    observer = Thread(target=observe_process, args=(pid, FILE,))
    observer.start()
    return FILE

def print_rss_chart(FILE):
    data = pd.read_csv(FILE,sep='\t', header=(0))
    data.time = pd.to_datetime(data.time)
    lock.acquire()
    plt.plot(data.time,data.rss)
    plt.title('Portion of memory occupied by a task in RAM [rss]')
    plt.xlabel('time')
    plt.ylabel('RAM usage [Mb]')
    plt.show()
    lock.release()

def print_cpu_chart(FILE):
    data = pd.read_csv(FILE,sep='\t', header=(0))
    data.time = pd.to_datetime(data.time)
    lock.acquire()
    plt.plot(data.time,data.cpu)
    plt.title('Cpu usage')
    plt.xlabel('time')
    plt.ylabel('total cores: [100% is one core]')
    plt.show()
    lock.release()

def print_write_read_operations_chart(FILE):
    data = pd.read_csv(FILE,sep='\t', header=(0))
    data.time = pd.to_datetime(data.time)
    lock.acquire()
    plt.plot(data.time,data.read,label='read')
    plt.plot(data.time,data.write,label='write')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    plt.title('Read/write operations')
    plt.xlabel('time')
    plt.ylabel('Mb')
    plt.show()
    lock.release()

def test_fusion(): #for testing purposes only
    command ='Rscript ./FUSION.assoc_test.R --sumstats ./OUTPUT/result.sumstats --weights ./INPUT/input1/WEIGHTS/GTEx.Whole_Blood.pos --weights_dir ./INPUT/input1/WEIGHTS/ --ref_ld_chr ./LDREF/1000G.EUR. --chr 22 --out ./OUTPUT/PGC2.SCZ.22.dat'
    cwd = "/home/x/DEVELOPER1/WORK/inzynierka/imputation_methods_comparison/methods/FUSION"
    method_name = 'fusion'
    FILE = getOutputPath(method_name)
    process = subprocess.Popen(command, shell=True, cwd=cwd)
    observer = Thread(target=observe_process, args=(process.pid,FILE,))
    observer.start()
    observer.join()
    print('observer joined')
    print_rss_chart(FILE)
    print_cpu_chart(FILE)
    print_write_read_operations_chart(FILE)

def test_predixcan(): #for testing purposes only
    command = './PrediXcan.py --predict --assoc --linear --weights weights/TW_Cells_EBV-transformed_lymphocytes_0.5.db --dosages genotype --samples samples.txt --pheno phenotype/igrowth.txt --output_prefix ./OUTPUT/Cells_EBV-transformed_lymphocytes'
    cwd ="/home/x/DEVELOPER1/WORK/inzynierka/imputation_methods_comparison/methods/PREDIXCAN"
    method_name = 'predixcan'
    FILE = getOutputPath(method_name)
    process = subprocess.Popen(command, shell=True, cwd=cwd)
    observer = Thread(target=observe_process, args=(process.pid,FILE,))
    observer.start()
    observer.join()
    print('observer joined')
    print_rss_chart(FILE)
    print_cpu_chart(FILE)
    print_write_read_operations_chart(FILE)

if __name__ == "__main__":
    # test_fusion()
    test_predixcan()

    # execute_bash_script("./tigar.sh", '../methods/TIGAR/SRC')
    # execute_bash_script("./metaxcan.sh",'../methods/METAXCAN/SRC')
    # execute_bash_script("./tests/script.sh",'.')

    # print_rss_chart()
    # print_cpu_chart()
    # print_write_read_operations_chart()


