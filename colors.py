import pandas as pd
import sys
import matplotlib.pyplot as plt
df = pd.read_csv("trafficdata.csv",encoding ='latin1')
Colors=df['Color']
Counts=[]
ColorsRed=[]
colors=["0","0","0","0","0","0","0","0"]
counts=[0,0,0,0,0,0,0,0]
labels=["0","0","0","0","0","0","0","0"]
s=0
summ=0
for col in Colors:
    col=str(col)
    col=col.replace(', DK', '')
    col=col.replace(', LGT', '')
    col=col.replace(', DARK', '')
    col=col.replace(', LIGHT', '')
    col=col.replace('CREAM', 'WHITE')
    col=col.replace('TAN', 'BROWN')
    col=col.replace('BEIGE', 'WHITE')
    col=col.replace('MAROON', 'RED')
    truth=False
    s=len(ColorsRed)-1

    if(col=="nan"):
        truth=True
   
    while s!=-1 and truth==False:
        if (col==ColorsRed[s]):
            Counts[s]=Counts[s]+1
            truth=True
            break
                                                                 
        s=s-1
 
    if (truth==False):
        ColorsRed.append(col)
        Counts.append(1)
for i in range(0,len(ColorsRed)):
    print(ColorsRed[i])
    print(Counts[i])
for i in range(0,8):
    colors[i]=ColorsRed[i]
    counts[i]=Counts[i]
for o in range(8,len(ColorsRed)):
    if (min(counts)<Counts[o]):
        summ=summ+min(counts)
        counts[counts.index(min(counts))]=Counts[o]
        colors[counts.index(Counts[o])]=ColorsRed[o]
    else:
        summ=summ+Counts[o]
for i in range(0,8):
    labels[i]=colors[i]
    if (colors[i]=="BLACK"):
        colors[i]='dimgray'
labels.append("OTHER")
counts.append(summ)
colors.append("ORANGE")

sizes=counts
plt.figure(1)
plt.pie(sizes,labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.figure(2)
plt.pie([22.5,19,16,15.5,10,7.5,6,2.5,1],labels=["WHITE","BLACK", "SILVER","GRAY","RED","BLUE","BROWN","GREEN","OTHER"],  colors=["WHITE","dimgray", "SILVER","GRAY","RED","BLUE","BROWN","GREEN","ORANGE"],
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.show()
