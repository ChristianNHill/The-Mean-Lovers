import math
import statistics
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
times = []
Datesy1 = []
Datesy2 = []
Datesy3 = []
Datesy4 = []
Datesy5 = []
df = pd.read_csv("trafficdata.csv",encoding ='latin1')
Dates=df['Date Of Stop']
Times=df['Time Of Stop']
PropDamage=df['Property Damage']
Accident=df['Contributed To Accident']
PersInjur=df['Personal Injury']
NewDates=[]
NewTimes=[]
for s in range(0,len(PropDamage)):
    if (PersInjur[s]=="Yes"):
        NewDates.append(Dates[s])
        NewTimes.append(Times[s])
for num in NewDates:
     s=1
     for numb in num.split('/'):
            if s==1:
                  month=int(numb)
            if s==3 and numb=="12":
                  Datesy1.append(month)
            if s==3 and numb=="13":
                  Datesy2.append(month)
            if s==3 and numb=="14":
                  Datesy3.append(month)
            if s==3 and numb=="15":
                  Datesy4.append(month)
            if s==3 and numb=="16":
                  Datesy5.append(month)
            s=s+1
for num in NewTimes:
      s=1
      for numb in num.split(':'):
            if s==1:
                  times.append(int(numb))
            s=s+1
plt.figure(1)
bins=[1,2,3,4,5,6,7,8,9,10,11,12,13]
plt.xticks(bins)
plt.hist(Datesy1, bins=bins)    
plt.title("Frequency of Traffic Violations in 2012")
plt.xlabel("Months of Year")
plt.ylabel("Frequency")

plt.figure(2)
plt.xticks(bins)
plt.hist(Datesy2, bins=bins)    
plt.title("Frequency of Traffic Violations in 2013")
plt.xlabel("Months of Year")
plt.ylabel("Frequency")

plt.figure(3)
plt.xticks(bins)
plt.hist(Datesy3, bins=bins)    
plt.title("Frequency of Traffic Violations in 2014")
plt.xlabel("Months of Year")
plt.ylabel("Frequency")

plt.figure(4)
plt.xticks(bins)
plt.hist(Datesy4, bins=bins)    
plt.title("Frequency of Traffic Violations in 2015")
plt.xlabel("Months of Year")
plt.ylabel("Frequency")

 
plt.figure(5)
plt.xticks(bins)
plt.hist(Datesy5, bins=bins)    
plt.title("Frequency of Traffic Violations in 2016")
plt.xlabel("Months of Year")
plt.ylabel("Frequency")

plt.figure(6)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
plt.hist(times, bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])    
plt.title("Frequency of Crashes Over 24 Hours")
plt.xlabel("Hour")
plt.ylabel("Frequency")

plt.figure(7)
plt.xticks(bins)
plt.hist(Datesy1+Datesy2+Datesy3+Datesy4+Datesy5, bins=bins)    
plt.title("Frequency of Crashes from 2012 to 2016")
plt.xlabel("Months of Year")
plt.ylabel("Frequency")



plt.show()
