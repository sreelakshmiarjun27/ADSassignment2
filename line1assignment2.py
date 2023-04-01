# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:36:25 2023

@author: BIJI PC
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns


data_fossil = pd.read_csv("Fossil.csv")
data_fossil.drop(['Country Code','Indicator Name'],axis=1,inplace=True)
df = data_fossil.set_index('Country Name',inplace =True)

years = list(map(str, range(2004,2009)))
df1 =data_fossil.loc[['Brazil','Botswana','Germany','Denmark','Italy'],years]
print(df1)
data1 = df1.transpose()
print(data1)
data1.plot(kind ='line')
plt.legend(loc ='best',fontsize = '10')

plt.show()