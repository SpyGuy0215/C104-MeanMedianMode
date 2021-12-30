import numpy as np
import csv
from scipy import stats
from colorama import Fore, Back, Style, init

init()

data = csv.reader(open('./SOCR-HeightWeight (1).csv', 'r'))
parsed_data = list(data)

parsed_data.pop(0)

weight = []

for i in parsed_data:
    weight.append(float(i[1]))

print('\n')
print(Fore.BLUE + 'Mean: ' + Fore.YELLOW + str(np.mean(weight)))
print(Fore.BLUE + 'Median: ' + Fore.YELLOW + str(np.median(weight)))
print(Fore.BLUE + 'Mode: ' + Fore.YELLOW + str(stats.mode(weight).mode[0]))
print('\n' + Style.RESET_ALL)