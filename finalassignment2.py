# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:13:04 2023

@author: BIJI PC
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns


def read_data(fn):
    """ 
    This function read data 
    """

    df = pd.read_csv(fn)
    return df


def bargraph1():
    """
    This function gives information regarding Total Population 
    of different countries in the year 2004,2005,2006

    """
    #Read the data
    df_population = read_data(
        r"C:\Users\BIJI PC\Desktop\data sci\ADS\assignment2\Population total.csv")
    #To Transpose the data
    df = df_population.transpose()
    #To fill Nan with 0
    df1 = df_population.fillna(0)
    #prints df1
    print(df1)
    #To select particular years
    val = df_population[['Country Name', '2004', '2005', '2006']]
    #To select specific Rows and Columns
    t = val.loc[0:4]
    print(t)
    y = t['Country Name']
    #To calculate some statistical data
    x = t.describe()
    print(x)
    #To create numeric sequences
    xpos = np.arange(len(y))
    xpos
    #To create figure
    plt.figure(figsize=(10, 4))
    #Sets the barwidth
    barwidth = 0.2
    #To plot Bar graph
    plt.bar(xpos, t['2004'], color="red", width=barwidth)
    plt.bar(xpos+0.2, t['2005'], color="yellow", width=barwidth)
    plt.bar(xpos+0.4, t['2006'], color="black", width=barwidth)
    #To set the current ticks on X-axis
    plt.xticks(xpos+0.3, ('Brazil', 'Botswana', 'Germany', 'Denmark', 'Italy'))
    #To set the Y-axis
    plt.yticks(fontsize=15)
    #Add Title
    plt.title("Total Population", fontsize=15)
    #To add labels
    plt.legend(['2004', '2005', '2006'], fontsize=15)
    #To add X-labels
    plt.xlabel("Country", fontsize=15)
    #To Add Y-labels
    plt.ylabel("Population", fontsize=15)
    #To save the plot
    plt.savefig("population.png")
    #Calculates skew for year 2004
    print("skew:", stats.skew(t["2004"]))
    #show the plot
    plt.show()
    #To get the mean
    _mean = val.mean()
    #To get the median
    _median = val.median()
    #To get mode
    _mode = stats.mode(val)
    print("Mean :\n", _mean)
    print("\n")
    print("Median :\n", _median)
    print("Mode :\n", _mode)


def bargraph2():
    """
    This function gives information regarding Total Greenhouse Gas Emissions
    of different countries in the year 2004,2005,2006

    """
    #Read the data
    df_greenhouse = read_data(
        r"C:\Users\BIJI PC\Desktop\data sci\ADS\assignment2\Greenhouse.csv")
    #To Transpose the data
    df = df_greenhouse.transpose()
    print(df)
    #To select particular years
    val = df_greenhouse[['Country Name', '2004', '2005', '2006']]
    #To select specific rows and columns
    t = val.loc[0:4]
    print(t)
    y = t['Country Name']
    #To calculate some statistical data
    x = t.describe()
    print(x)
    #To create numeric sequences
    xpos = np.arange(len(y))
    xpos
    #To create figure
    plt.figure(figsize=(10, 4))
    #Sets the barwidth
    barwidth = 0.2
    #To plot Bar graph
    plt.bar(xpos, t['2004'], color="green", width=barwidth)
    plt.bar(xpos+0.2, t['2005'], color="orange", width=barwidth)
    plt.bar(xpos+0.4, t['2006'], color="black", width=barwidth)
    #To find correlation in each column
    v = t.corr()
    print(v)
    #To set the current ticks on X-axis
    plt.xticks(xpos+0.3, ('Brazil', 'Botswana', 'Germany',
               'Denmark', 'Italy'), fontsize=15)
    #To set the Y-axis
    plt.yticks(fontsize=15)
    #To add labels
    plt.legend(['2004', '2005', '2006'])
    #To set the title
    plt.title("Total Greenhouse gas emissions", fontsize=15)
    #To add X-labels
    plt.xlabel("Country", fontsize=15)
    #To add Y-labels
    plt.ylabel("Greenhouse gas emission", fontsize=15)
    #To save the plot
    plt.savefig("Total Greenhouse gas emissions.png")
    #To show the plot
    plt.show()
    #To get the mean
    _mean = val.mean()
    #To get the median
    _median = val.median()
    #To get the mode
    _mode = stats.mode(val)
    print("Mean :\n", _mean)
    print("\n")
    print("Median :\n", _median)
    print("Mode :\n", _mode)


def linegraph1():
    """
    This function plots the Fossil fuel energy consumption in different countries 
    from the year 2004-2008
    
    """
    #Read the data
    data_fossil = read_data(
        r"C:\Users\BIJI PC\Desktop\data sci\ADS\assignment2\Fossil.csv")
    #To remove specified row or column
    data_fossil.drop(['Country Code', 'Indicator Name'], axis=1, inplace=True)
    #To set the dataframe index
    df = data_fossil.set_index('Country Name', inplace=True)
    #To store data
    years = list(map(str, range(2004, 2009)))
    #To select specified row or column
    df1 = data_fossil.loc[['Brazil', 'Botswana',
                           'Germany', 'Denmark', 'Italy'], years]
    print(df1)
    #To transpose the data
    data1 = df1.transpose()
    print(data1)
    #To group large amount of data and perform specific operations on the group
    x = data_fossil.groupby(['2020']).agg('sum', 'mean')
    #To plot line graph
    data1.plot(kind='line')
    #To add labels
    plt.legend(loc='best', fontsize='10')
    #To set the title
    plt.title("Fossil fuel energy consumption ", fontsize=15)
    #To add X-labels
    plt.xlabel("Years", fontsize=15)
    #To add Y-labels
    plt.ylabel("Fossil fuel energy consumption", fontsize=15)
    #To save the plot
    plt.savefig("Fossil fuel .png", bbox_inches="tight", dpi=300)
    #To show the plot
    plt.show()


def linegraph2():
    """
    This function gives information regarding Nitrous oxide emissions in energy sector
    of different countries from the year 2004-2008
    
    """
    #Read the data
    data_gas = read_data("nitrousoxide.csv")
    #To remove specified row or column
    data_gas.drop(['Country Code', 'Indicator Name'], axis=1, inplace=True)
    #To set the dataframe index
    df = data_gas.set_index('Country Name', inplace=True)
    #To store data
    years = list(map(str, range(2004, 2009)))
    df1 = data_gas.loc[['Brazil', 'Botswana',
                        'Germany', 'Denmark', 'Italy'], years]
    print(df1)
    data1 = df1.transpose()
    print(data1)
    #To plot line graph
    data1.plot(kind='line', figsize=(10, 4))
    #To add labels
    plt.legend(fontsize="7")
    #To set the title
    plt.title("Nitrous oxide emissions in energy sector", fontsize=15)
    #To add X-labels
    plt.xlabel("Years", fontsize=15)
    #To add Y-labels
    plt.ylabel("Nitrous oxide emissions in energy sector", fontsize=15)
    #To save the plot
    plt.savefig("Nitrous oxide emissions.png", bbox_inches="tight")
    #To show the plot
    plt.show()


def heatmap():
    """
    This function visualize correlation between different indicators

    """
    #Read the data
    df_brazil = read_data("brazil.csv")
    #To remove specified row or column
    df_drop = df_brazil.drop("Time", axis=1)
    #To transpose the data
    df_trans = df_drop.transpose()
    print(df_trans)
    data = df_drop.corr()
    #To create heatmap
    sns.heatmap(data, annot=True, cmap="rocket")
    plt.plot()
    #To set title
    plt.title("Brazil", fontsize=15)
    plt.xticks(rotation=90, horizontalalignment="center", fontsize=10)
    plt.yticks(fontsize=15)
    #To save the plot
    plt.savefig("Heatmap.png", bbox_inches="tight")
    #To show the plot
    plt.show()


if __name__ == "__main__":

    #calling function to visualise bar plot
    bargraph1()

    #calling function to visualise bar plot
    bargraph2()

    #calling function to visualise line plot
    linegraph1()

    #calling function to visualise line plot
    linegraph2()

    #calling function to visualise heatmap
    heatmap()
