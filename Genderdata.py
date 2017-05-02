import math
import statistics
import sys
import numpy as np
import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import pandas as pd
genders=["Male","Female"]
Citations = [0,0]
Warnings= [0,0]

df = pd.read_csv("trafficdata.csv",encoding ='latin1')
Gen=df['Gender']
Cit=df['Violation Type']
s=0
for num in Gen:
     if (num=="M") and (Cit[s]=="Citation"):
          Citations[0]=Citations[0]+1
     elif (num=="M") and (Cit[s]=="Warning"):
          Warnings[0]=Warnings[0]+1
     elif (num=="F") and (Cit[s]=="Warning"):
          Warnings[1]=Warnings[1]+1
     elif (num=="F") and (Cit[s]=="Citation"):
          Citations[1]=Citations[1]+1
     s=s+1
 
plotly.tools.set_credentials_file(username='chasewhyte', api_key='ovBmY7BJeSUzXvMgTgfx')
py.sign_in("chasewhyte", "ovBmY7BJeSUzXvMgTgfx")



trace1 = go.Bar(
    x=genders,
    y=Citations,
    name='Citations'
)
trace2 = go.Bar(
    x=genders,
    y=Warnings,
    name='Warnings'
)

data = [trace2, trace1]
layout = go.Layout(
    barmode='stack',yaxis=dict(
        title='Number of Occurrences')
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

