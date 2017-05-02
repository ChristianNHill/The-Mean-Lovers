import sys
import pandas as pd
df = pd.read_csv("trafficdata.csv",encoding ='latin1')
PropDamage=df['Property Damage']
Accident=df['Contributed To Accident']
Street=df['Location']
Location=df['Geolocation']
file=open("Geolocations.txt",'w')
s=0
while s!=30000:
    if (Accident[s]=="Yes") or (PropDamage[s]=="Yes"):
        file.write(Street[s])
        file.write(" ")
        file.write(str(Location[s]))
        file.write("\n")
    s=s+1
