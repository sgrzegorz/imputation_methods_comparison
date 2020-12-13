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
    return bytes/1048576


def getOutputPath(method_name):
    timestamp = str(time.strftime("%Y-%m-%d_%H-%M-%S"))
    return f'{ROOT_DIR}/output/resources/{method_name}{timestamp}.csv'


def _stats_with_children(process,writer):
    try:
        rss = process.memory_full_info().rss
        swap = process.memory_full_info().swap
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

        rss =_bytes_to_megabytes(rss)
        swap=_bytes_to_megabytes(swap)
        read =_bytes_to_megabytes(read_bytes)
        write=_bytes_to_megabytes(write_bytes)
        writer.writerow((now,rss,swap,cpu,read,write))
    except psutil.NoSuchProcess as e: 
        print('Dont worry :) -one of obeserved imputation method subprocesses disappeard')
        

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

    num_lines = sum(1 for line in open(FILE))
    if num_lines<2:
        os.remove(FILE)
        print("Result resources log was removed,because it was too short!")


def observe_imputation_process(pid,method_name):
    FILE = getOutputPath(method_name)
    observer = Thread(target=observe_process, args=(pid, FILE,))
    observer.start()
    return FILE


if __name__ == "__main__":


    pass
