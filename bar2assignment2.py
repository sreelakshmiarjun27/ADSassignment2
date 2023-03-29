# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:56:31 2023

@author: sreelakshmi vinod
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns

df = pd.read_csv("Population total.csv")
#print(df)
#df = df.transpose()
#df1 = df.dropna(subset=['1960','1961','1962'])
#print(df1)

val = df[['Country Name','2017', '2018', '2019']]
t = val.loc[0:4]
print(t)
y = t['Country Name']
x = t.describe()
print(x)
xpos = np.arange(len(y))
xpos
plt.figure(figsize=(10,4))
barwidth = 0.2
plt.bar(xpos,t['2017'],color="red",width=barwidth)
plt.bar(xpos+0.2,t['2018'],color="orange",width=barwidth)
plt.bar(xpos+0.4,t['2019'],color="blue",width=barwidth)
plt.xticks(xpos+0.3,('Australia','China','India','United Kingdom','United States'))
#plt.bar(X,Y,width=0.8)
#plt.yticks([0,1,2,3,4,5,6,7])
plt.show()
_mean =val.mean()
_median =val.median()
_mode = stats.mode(val)
print("Mean :\n",_mean)
print("\n")
print("Median :\n",_median)  
print("Mode :\n",_mode)