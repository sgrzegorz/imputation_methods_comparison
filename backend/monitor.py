import datetime
import errno
import os,subprocess,sys
import resource
import time
import psutil
import pandas as pd
import matplotlib.pyplot as plt
import traceback


from threading import Thread
from time import sleep
STATISTICS_FILE_PATH = '/tmp/statistics.txt'
import threading
lock = threading.Lock()

def execute_bash_script(filename, relative_path):
    start = time.time()

    origWD = os.getcwd()  # remember our original working directory
    os.chdir(os.path.join(os.path.abspath(sys.path[0]),
                          relative_path))
    imputation_process = subprocess.Popen([filename], stdout=subprocess.PIPE,
                               shell=True)
    print('komenda zabicia procesu imuptacji i wszystkich jego potomkow:')
    print(f"pstree -p {imputation_process.pid} | grep -o '([0-9]\+)' | grep -o '[0-9]\+' | xargs -n1 kill -15")

    observer = Thread(target=observe_process, args=(imputation_process.pid,))
    observer.start()


    # print stdout
    for line in iter(imputation_process.stdout.readline, b''):
        print(line)
    imputation_process.stdout.close()
    print('Joining begins')

    imputation_process.wait()
    print('imputation process joined')

    observer.join()
    print('observer joined')
    os.chdir(origWD)  # get back to our original working directory

    total_time =time.time() -start

    print('Total time [s]: ', total_time)
    return total_time

def _bytes_to_megabytes(bytes):
    return bytes/1000000

def stats_with_children(process,file):
    # obciazenie ram w bajtach
    rss = process.memory_full_info().rss
    swap = process.memory_full_info().swap
    # obciazenie rdzenia cpu w procentach jak wiecej niz 100% to pracuje na wiecej niz 1 rdzeniu
    cpu =process.cpu_percent(interval=0.1)

    user  =process.cpu_times().user
    system = process.cpu_times().system

    read_bytes = process.io_counters().read_bytes
    write_bytes = process.io_counters().write_bytes

    now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    try:
        for child in process.children(recursive=True):
            rss += child.memory_full_info().rss
            swap += child.memory_full_info().swap
            cpu+=child.cpu_percent(interval=0.1)
            user += child.cpu_times().user
            system += child.cpu_times().system

            read_bytes += child.io_counters().read_bytes
            write_bytes += child.io_counters().write_bytes

    except psutil.NoSuchProcess as e: # jedno z dzieci nagle przestalo byc zywe
        print(traceback.format_exc())


    rss =_bytes_to_megabytes(rss)
    swap=_bytes_to_megabytes(swap)
    read =_bytes_to_megabytes(read_bytes)
    write=_bytes_to_megabytes(write_bytes)
    file_line =f"{now}\t{rss}\t{swap}\t{cpu}\t{read}\t{write}\n"
    file.write(file_line)
    print(file_line,end='')

def observe_process(pid):
    with open(STATISTICS_FILE_PATH, 'w+') as file:
        try:
            file_line = f"time\trss\tswap\tcpu\tread\twrite\n"
            file.write(file_line)
            while(psutil.pid_exists(pid)):
                process = psutil.Process(pid=pid)
                stats_with_children(process,file)

                sleep(1)
        except Exception as e:
            # Proces który obserwuejmy sie zakonczyl albo wystapil nieoczekiwany blad
            print('Observer returns------------------------------------------')
            print(traceback.format_exc())
            print('Observer returned------------------------------------------')
            pass

def print_rss_chart():
    data = pd.read_csv(STATISTICS_FILE_PATH,sep='\t', header=(0))
    data.time = pd.to_datetime(data.time)
    lock.acquire()
    plt.plot(data.time,data.rss)
    plt.title('Portion of memory occupied by a task in RAM [rss]')
    plt.xlabel('time')
    plt.ylabel('RAM usage [Mb]')
    plt.show()
    lock.release()

def print_cpu_chart():
    data = pd.read_csv(STATISTICS_FILE_PATH,sep='\t', header=(0))
    data.time = pd.to_datetime(data.time)
    lock.acquire()
    plt.plot(data.time,data.cpu)
    plt.title('Cpu usage')
    plt.xlabel('time')
    plt.ylabel('total cores: [100% is one core]')
    plt.show()
    lock.release()

def print_write_read_operations_chart():
    data = pd.read_csv(STATISTICS_FILE_PATH,sep='\t', header=(0))
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

if __name__ == "__main__":
    execute_bash_script("./predixcan.sh",'../methods/PREDIXCAN/SRC')
    # execute_bash_script("./tigar.sh", '../methods/TIGAR/SRC')
    # execute_bash_script("./metaxcan.sh",'../methods/METAXCAN/SRC')
    # execute_bash_script("./tests/script.sh",'.')

    print_rss_chart()
    print_cpu_chart()
    print_write_read_operations_chart()


