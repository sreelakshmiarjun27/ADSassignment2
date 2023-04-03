# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:23:10 2023

@author: BIJI PC
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns

    
def heatmap():
    """
    This function visualize correlation between different indicators

    """
    #Read the data
    df_brazil = pd.read_csv("brazil.csv")
    #To remove specified row or column
    df_drop = df_brazil.drop("Time",axis=1)
    #To transpose the data
    df_trans = df_drop.transpose()
    print(df_trans)
    
    data = df_drop.corr()
    #sns.heatmap(data)
    sns.heatmap(data, annot = True,cmap ="mako")
    plt.plot()
    plt.title("Brazil",fontsize=15)
    plt.xticks(rotation=90,horizontalalignment="center",fontsize=15)
    plt.yticks(fontsize=15)
    #To save the plot
    plt.savefig("Heatmap.png", bbox_inches = "tight")
    #To show the plot
    plt.show()    
    
heatmap()