import os

PREDIX_PATH = 'methods/PrediXcanExample'



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

def execute_predixcan_method():
    predixcan_command =  f'cd {PREDIX_PATH} && python3 PrediXcan.py --predict --assoc --linear  --weights weights/TW_Cells_EBV-transformed_lymphocytes_0.5.db    --dosages genotype       --samples samples.txt       --pheno phenotype/igrowth.txt       --output_prefix results/Cells_EBV-transformed_lymphocytes '
    os.system(predixcan_command)

if __name__ == "__main__":
    execute_predixcan_method()

