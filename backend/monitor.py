import datetime
import errno
import os,subprocess,sys
import resource
import time
import psutil
import pandas as pd
import matplotlib.pyplot as plt


from threading import Thread
from time import sleep


def execute_bash_script(filename, relative_path):
    # start = time.time()
    origWD = os.getcwd()  # remember our original working directory
    os.chdir(os.path.join(os.path.abspath(sys.path[0]),
                          relative_path))
    process = subprocess.Popen([filename], stdout=subprocess.PIPE,
                               shell=True)
    print("PID " ,process.pid)

    observer = Thread(target=observer_function, args=(10,process.pid,))
    observer.start()


    # print stdout child processu
    for line in iter(process.stdout.readline, b''):
        print(line)
    process.stdout.close()
    process.wait()

    observer.join()

    os.chdir(origWD)  # get back to our original working directory

    # end = time.time()
    # print('Total time [s]: ', end-start)

def observer_function(arg,pid):
    with open('/tmp/rss.txt', 'w') as file:
        try:
            file.write(f"rss\ttime\n")
            while(True):
                process = psutil.Process(pid)
                print(process.create_time())
                print(process.memory_full_info(), process.cpu_percent())  # in bytes
                now =datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                rss_mb = process.memory_full_info().rss /1000000
                swap =process.memory_full_info().swap /1000000
                file.write(f"{rss_mb}\t{now}\t{swap}\n")
                print(process.cpu_times())
                # p=resource.getrusage(pid).ru_maxrss
                # print("running", p)
                sleep(1)
        except Exception as e:
            # Proces który obserwuejmy sie zakonczyl albo wystapil nieoczekiwany blad
            print('Observer returns')
            pass

def print_rss_chart():
    data = pd.read_csv('/tmp/rss.txt',sep='\t', header=(0))
    data.time = pd.to_datetime(data.time)
    # data['time'] =data['time'].apply(lambda x: datetime.datetime.strptime(x,"%m/%d/%Y, %H:%M:%S"))
    # data['time'] = [datetime.datetime.strptime(x,"%m/%d/%Y, %H:%M:%S") for x in data['time']]
    plt.plot(data.time,data.rss)
    plt.title('Portion of memory occupied by a task in RAM [rss]')
    plt.xlabel('time')
    plt.ylabel('RAM [mb]')
    plt.show()
    

if __name__ == "__main__":
    execute_bash_script("./predixcan.sh",'../methods/PrediXcanExample/SRC')

    # execute_bash_script("./metaxcan.sh",'../methods/MetaXcan/SRC')
    # execute_bash_script("./script.sh",'.')

    print_rss_chart()

    # thread = Thread(target = observer_function, args = (10, ))
    # thread.start()
    # thread.join()
    # print("thread finished...exiting")
