# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 01:32:32 2018

@author: Student
"""
N=10000

import numpy as np
import pandas as pd
import math 






raw_data={'f11': [8123,8330,3954,2886,1500,4000,9841,4000,7450,61],
          'f10':[83,2,3080,1363,2000,2000,298,2000,2483,2483],
          'f01':[424,622,5,1320,500,1000,127,2000,4,4],
          'f00':[1370,1046,2961,4431,6000,3000,94,2000,63,7452]}



df = pd.DataFrame(raw_data, columns = ['f11', 'f10', 'f01', 'f00'],dtype=float)

df['f1+']=df['f11']+df['f10']
df['f0+']=df['f01']+df['f00']
df['f+1']=df['f01']+df['f11']
df['f+0']=df['f00']+df['f10']

symmetric_measures={}

df1= pd.DataFrame(symmetric_measures,dtype=float)

df1['correlation']=((N)*(df['f11'])-(df['f1+'])*(df['f+1']))
df1['correlation']=df1['correlation'].astype(float)/(((df['f10'])*(df['f01'])*(df['f0+'])*(df['f+0']))**(0.5))

df1['oddsR']=(df['f11']*df['f00'])/(df['f10']*df['f01'])

df1['Kappa']=(N*df['f11']+N*df['f00']-df['f1+']*df['f+1']-df['f0+']*df['f+0'])/(N*N-df['f1+']*df['f+1']-df['f0+']*df['f+0'])

df1['Interest']=(N*df['f11'])/(df['f1+']*df['f+1'])

df1['Piatetsky Shapiro(PS)']=(df['f11']/N)-(df['f1+']*df['f+1'])/N;
    
df1['Collective Strength']=(df['f11']+df['f00'])*(N-df['f1+']*df['f+1']-df['f0+']*df['f+0'])/((df['f1+']*df['f+1']+df['f0+']*df['f+0'])*(N-df['f11']-df['f00']))

df1['Jaccard']=df['f11']/(df['f1+']+df['f+1']-df['f11'])

df1['v1']=(df['f11']/df['f1+'])
df1['v2']=(df['f11']/df['f+1'])

df1['AllConfidence']=df1[['v1','v2']].min(axis=1)

asymmetric_measures={}
df2=pd.DataFrame(asymmetric_measures,dtype=float)

df2['Gini_Index']=((df['f1+']/N)*((df['f11']/df['f1+'])**2)+((df['f10']/df['f1+'])**2))-(df['f+1']/N)+((df['f0+']/N)*((df['f01']/df['f0+'])**2)+((df['f00']/df['f0+'])**2))-((df['f+0']/N)**2)

df2['Laplace']=(df['f11']+1)/(df['f1+']+2);

df2['Conviction']=(df['f1+']*df['f+0'])/(df['f10']*N);

df2['Certainity Factor']=((df['f11']/df['f1+'])-(df['f+1']/N))/(1-df['f+1']/N);

df2['Added Value']=((df['f11']/df['f1+'])-(df['f+1']/N))

df2['J-Measure']=(df['f11']/N)*(np.log(N*df['f11']/df['f+1']))+(df['f10']/N)*(np.log(N*df['f10']/df['f1+']*df['f+0']))

df2['Mutual Information']=(-1)*((df['f00']/N)*np.log(df['f00']/(df['f0+']*df['f+0']))+(df['f01']/N)*np.log(df['f01']/(df['f0+']*df['f+1']))+(df['f10']/N)*np.log(df['f10']/(df['f1+']*df['f+0']))+(df['f11']/N)*np.log(df['f11']/(df['f1+']*df['f+1'])))/((df['f0+']/N)*np.log(df['f0+']/N)+(df['f1+']/N)*np.log(df['f1+']/N))

#print(df)


