# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 19:18:45 2023

@author:  BIJI PC
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns


data_gas = pd.read_csv("nitrousoxide.csv")
data_gas.drop(['Country Code','Indicator Name'],axis=1,inplace=True)
df = data_gas.set_index('Country Name',inplace =True)

years = list(map(str, range(2004,2009)))
df1 =data_gas.loc[['Brazil','Botswana','Germany','Denmark','Italy'],years]
print(df1)
data1 = df1.transpose()
print(data1)
data1.plot(kind ='line',figsize=(10,4))
plt.legend(fontsize ="7")
plt.title("Fossil",fontsize=15)
plt.xlabel("Years",fontsize=15)
plt.ylabel("Fossil",fontsize=15)
plt.show()