import os
import json
import subprocess
import sys
from json import JSONEncoder

PREDIX_PATH = 'methods/PrediXcanExample'

class Message(JSONEncoder):
    def __init__(self,gene,beta,t,p,se_beta):
        self.gene = gene
        self.beta = beta
        self.t = t
        self.p = p
        self.se_beta = se_beta

    def default(self, o):
        return o.__dict__

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)


def parse_predixcan_results(filename = f'{PREDIX_PATH}/results/Cells_EBV-transformed_lymphocytes_association.txt'):
    with open(filename) as f:
        lines = f.readlines()  # list containing lines of file
        columns = []  # To store column names
        my_list = []
        i = 1
        for line in lines:
            line = line.strip()  # remove leading/trailing white spaces
            if line:
                if i == 1:
                    columns = [item.strip() for item in line.split(' ')]
                    i = i + 1
                else:
                    d = {}  # dictionary to store file data (each line)
                    data = [item.strip() for item in line.split(' ')]
                    for index, elem in enumerate(data):
                        d[columns[index]] = data[index]

                    message = Message(d['gene'],d['beta'],d['t'],d['p'],d['se(beta)'])
                    my_list.append(message)  # append dictionary to list

    # take only first 50 elements
    return my_list[:50]


def execute_bash_script(filename, relative_path):
    origWD = os.getcwd()  # remember our original working directory
    os.chdir(os.path.join(os.path.abspath(sys.path[0]),
                          relative_path))
    process = subprocess.Popen([filename], stdout=subprocess.PIPE,
                               shell=True)

    # print stdout child processu
    for line in iter(process.stdout.readline, b''):
        print(line)
    process.stdout.close()
    process.wait()

    os.chdir(origWD)  # get back to our original working directory


if __name__ == "__main__":
    execute_bash_script("./predixcan.sh",'../methods/PrediXcanExample/SRC')


