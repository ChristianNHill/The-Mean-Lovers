import numpy as np
import matplotlib as plt
import pdb
import collections
import csv
import pandas as pd
from pandas import *


data = read_csv('Traffic_Violations.csv')
#data2 = pd.read_csv('Personal_Injuries.csv', parse_dates=True)
data2 = pd.read_csv('Personal_Injury.csv', sep='\s+', parse_dates=[0])
data2.info()

number = collections.Counter()
number2 = collections.Counter()

with open('Traffic_Violations.csv') as input_file:
    for row in csv.reader(input_file, delimiter=','):
        number[row[10]] += 1
        number2[row[12]] += 1


print ('Number of Personal Injuries: %s' % number['Yes'])
print (number.most_common())
print ('Number of Fatal Injuries: %s' % number2['Yes'])
print (number2.most_common())

data['year'] = data['Date Of Stop'].dt.year
data['month'] = data['Date Of Stop'].dt.month

data2['date'] = pd.to_datetime(data2['date'])
data2['year'], data2['month'] = data2['date'].dt.year, data2['date'].dt.month

def ReadInAttributeFromCSV(fileName, attribute):
    attributeValues = []
    f = open(fileName, 'r')
    # Create a csv reader that stores the each column of the first line of the file
    # as keys and then the rest of the lines of each column as values for those keys
    reader = csv.DictReader(f)
    for row in reader:
        if attribute in row:
            if attribute != 'date':
                value = float(row[attribute])
                attributeValues.append(value)
            else:
                date = datetime.datetime.strptime(row[attribute], '%m/%d/%Y')
                attributeValues.append(date)
    f.close()
    return attributeValues

def Histogram(filename):
    volume = ReadInAttributeFromCSV(filename, 'Personal Injury')

    plt.title('Annual Personal Injury')
    plt.hist(volume, color='black')
    plt.ylabel('Number of')
    plt.xlabel('Seasons')
    plt.savefig('visual')
    plt.close()