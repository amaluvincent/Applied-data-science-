# -*- coding: utf-8 -*-



# Importing required packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import kurtosis 
from scipy.stats import skew 

def read_file(file_name):
    
    
    """
    This function takes name of the file and reads it from local directory and 
    loads it into a dataframe.
    Then transposes the dataframe and returns both the first and transposed 
    dataframes. It also sets the header for the transposed dataframe
    Parameters
    ----------
    file_name : string
        Name of the file to be read into the dataframe.
    Returns
    -------
    A dataframe loaded from the file and it's transpose.
    """


    df = pd.read_excel(file_name)
    df_transpose = pd.DataFrame.transpose(df)
    #Header setting
    header = df_transpose.iloc[0].values.tolist()
    df_transpose.columns = header
    return(df, df_transpose)

def clean_df(df_clean):
    """
    
    Parameters
    ----------
    df : dataframe
        Dataframe that needs to be cleaned and index converted.
    Returns
    -------
    df : dataframe
        dataframe with required columns and index as int.
    """
    #Cleaning the dataframe
    df_clean = df_clean.iloc[1:]
    df_clean = df_clean.iloc[30:58]
    
    #Converting index to int
    df_clean.index = df_clean.index.astype(int)
    df_clean = df_clean[df_clean.index > 1989]

    # Cleaning empty cells
    df_clean = df_clean.dropna(axis='columns')
    return df_clean


# Reading file 
df_arable_total,df_arable_countries = read_file("arable_land.xlsx")
df_greengas_totaldf_forest_total,df_forest_countries = read_file("forest_area.xlsx")



#creates a list of countries and years to use in the plot
countries = ['United Arab Emirates','China','Denmark','France','Gabon',
             'United Kingdom','Japan','Mozambique','United States','South Africa']
countries_label = ['UAE','CHN','DNK','FRA','GAB','UK','JPN','MOZ','USA','ZAF']
years = [1991,1995,2000,2005,2010]
  
"""
Arable land Bar graph
Creating bar graph of Total percentage of Arable land by mutiple
countries from 1991-2010
"""    

# Cleaning the dataframe
df_arable_countries = clean_df(df_arable_countries)

# selecting only required data
df_arable_perc = pd.DataFrame.transpose(df_arable_countries)
df_arable_subset_perc = df_arable_perc[years].copy()
df_arable_subset_perc = df_arable_subset_perc.loc[df_arable_subset_perc.index.
                                                  isin(countries)]

# plotting the data
n = len(countries) 
r = np.arange(n)
width = 0.1
plt.bar(r-0.3, df_arable_subset_perc[1991], color='deeppink',
        width=width, edgecolor='black', label='1991')
plt.bar(r-0.2, df_arable_subset_perc[1995], color='pink',
        width=width, edgecolor='black', label='1995')
plt.bar(r-0.1, df_arable_subset_perc[2000], color='coral',
        width=width, edgecolor='black', label='2000')
plt.bar(r, df_arable_subset_perc[2005], color='yellow',
        width=width, edgecolor='black', label='2005')
plt.bar(r+0.1, df_arable_subset_perc[2010], color='orange',
        width=width, edgecolor='black', label='2010')

plt.xlabel("Countries",fontweight='bold')
plt.ylabel("% of land",fontweight='bold')
plt.xticks(width+r, countries_label,rotation=30)
plt.legend()
plt.title("Arable Land (% of land area)",fontweight='bold')
plt.savefig("Arable _Land.png", dpi=300, bbox_inches='tight')
plt.show()

"""
Forest Land bar graph
Creating bar graph of percentage emissions (kt) of multiple countries from 
1991-2010
"""

# Cleaning the dataframe
df_forest_countries = clean_df(df_forest_countries)

# selecting only required data
df_forest_perc = pd.DataFrame.transpose(df_forest_countries)

df_forest_subset_perc = df_forest_perc[years].copy()

df_forest_subset_perc = df_forest_subset_perc.loc[df_forest_subset_perc.index.isin(countries)]

# plotting the data
plt.bar(r-0.3, df_forest_subset_perc[1991], color='aqua',
        width=width, edgecolor='black', label='1991')
plt.bar(r-0.2, df_forest_subset_perc[1995], color='turquoise',
        width=width, edgecolor='black', label='1995')
plt.bar(r-0.1, df_forest_subset_perc[2000], color='steelblue',
        width=width, edgecolor='black', label='2000')
plt.bar(r, df_forest_subset_perc[2005], color='deepskyblue',
        width=width, edgecolor='black', label='2005')
plt.bar(r+0.1, df_forest_subset_perc[2010], color='blue',
        width=width, edgecolor='black', label='2010')

plt.ticklabel_format(style='plain')
plt.xlabel("Countries",fontweight='bold')
plt.ylabel("% of land",fontweight='bold')
plt.xticks(width+r, countries_label, rotation=30)
plt.legend()
plt.title("Forest land (% of land area)",fontweight='bold')
plt.savefig("Forest.png", dpi=300, bbox_inches='tight')
plt.show()


# Reading files for line plots
df_access_co2, df_access_co2_countries = read_file("CO2_emmission.xls")
df_access_pop, df_access_pop_total = read_file("population.xlsx")

"""
CO2 emmission line graph
Creating line graph of percentage emissions (kt) of co2 for multiple countries
from 1991-2010
"""

  
df_access_co2_countries = df_access_co2_countries.iloc[1:]
df_access_co2_countries = df_access_co2_countries.iloc[34:55]
print(df_access_co2_countries)
df_access_co2_countries.index = df_access_co2_countries.index.astype(int)
df_access_co2_countries = df_access_co2_countries[df_access_co2_countries.index > 1989]

df_access_kt = pd.DataFrame.transpose(df_access_co2_countries)
print(df_access_kt)

df_access_subset_kt = df_access_kt[years].copy()
df_access_subset_kt = df_access_subset_kt.loc[df_access_subset_kt.index.isin(
    countries)]

print(df_access_subset_kt)
# plotting the data
plt.figure()

plt.plot(df_access_co2_countries .index, df_access_co2_countries["United Arab Emirates"],
         color='darkblue')
plt.plot(df_access_co2_countries.index, df_access_co2_countries["China"],
         color='skyblue')
plt.plot(df_access_co2_countries.index, df_access_co2_countries["Denmark"],
         color='coral')
plt.plot(df_access_co2_countries.index, df_access_co2_countries["France"],
         color='lightgreen')
plt.plot(df_access_co2_countries.index, df_access_co2_countries["Gabon"],
         color='orange')
plt.plot(df_access_co2_countries.index, df_access_co2_countries["United Kingdom"],
         color='brown')
plt.plot(df_access_co2_countries.index, df_access_co2_countries["Japan"],
         color='yellow')
plt.plot(df_access_co2_countries.index, df_access_co2_countries["Mozambique"],
         color='turquoise')
plt.plot(df_access_co2_countries.index, df_access_co2_countries["United States"],
         color='black')
plt.plot(df_access_co2_countries.index, df_access_co2_countries["South Africa"],
         color='pink')

plt.xlim(1991,2010)
plt.ticklabel_format(style='plain')
plt.xlabel("Year", fontsize=15, fontweight='bold')
plt.ylabel("CO2 emissions (kt)", fontsize=15, fontweight='bold')
plt.title("CO2 emissions (kt)", fontsize=15, fontweight='bold')
plt.savefig("co2.png", dpi=300,bbox_inches='tight')
plt.legend(countries_label)
plt.show()
"""
Total population line graph
Creating line graph of total population of multiple countries from 
1991-2010
"""
df_access_pop_total = df_access_pop_total.iloc[1:]
df_access_pop_total = df_access_pop_total.iloc[34:55]

df_access_pop_total.index = df_access_pop_total.index.astype(int)
df_access_pop_total = df_access_pop_total[df_access_pop_total.index > 1989]

df_access_pop = pd.DataFrame.transpose(df_access_pop_total)
print(df_access_pop)

df_access_subset_pop = df_access_pop[years].copy()
df_access_subset_pop = df_access_subset_pop.loc[df_access_subset_pop.index.isin(
    countries)]

print(df_access_subset_pop)
# plotting the data
plt.figure()

plt.plot(df_access_pop_total .index, df_access_pop_total["United Arab Emirates"],
         color='pink',linestyle="dashed")
plt.plot(df_access_pop_total.index, df_access_pop_total["China"],
         color='darkblue',linestyle="dashed")
plt.plot(df_access_pop_total.index, df_access_pop_total["Denmark"],
         color='coral',linestyle="dashed")
plt.plot(df_access_pop_total.index, df_access_pop_total["France"],
         color='lightgreen',linestyle="dashed")
plt.plot(df_access_pop_total.index, df_access_pop_total["Gabon"],
         color='orange',linestyle="dashed")
plt.plot(df_access_pop_total.index, df_access_pop_total["United Kingdom"],
         color='brown',linestyle="dashed")
plt.plot(df_access_pop_total.index, df_access_pop_total["Japan"],
         color='yellow',linestyle="dashed")
plt.plot(df_access_pop_total.index, df_access_pop_total["Mozambique"],
         color='red',linestyle="dashed")
plt.plot(df_access_pop_total.index, df_access_pop_total["United States"],
         color='aquamarine',linestyle="dashed")
plt.plot(df_access_pop_total.index, df_access_pop_total["South Africa"],
         color='black',linestyle="dashed")

plt.xlim(1991,2010)
plt.ticklabel_format(style='plain')
plt.xlabel("Year", fontsize=15, fontweight='bold')
plt.ylabel("Population", fontsize=15, fontweight='bold')
plt.title("Total Population)", fontsize=15, fontweight='bold')
plt.legend(countries_label)
plt.savefig("pop.png", dpi=300, bbox_inches='tight')
plt.show()




def country_df(country_name):
    """
    Creates a dataframe for the country with Arable land,Forest land,co2 emission,
    and Total Population as columns
    Parameters
    ----------
    country_name : string
        Name of the country to create the dataframe.
    Returns
    -------
    df_name : dataframe
        Newly created dataframe.
    """

    # creates dataframe name
    df_name = "df_" + country_name
    # creates dataframe
    df_name = pd.concat([df_arable_countries[country_name].astype(float),
                         df_forest_countries[country_name].astype(float),
                         df_access_co2_countries[country_name].astype(float),
                         df_access_pop_total[country_name].astype(float)], axis=1)
    print(df_access_co2_countries)
    # Gives column names
    df_name.columns.values[0] = "Arable Land"
    df_name.columns.values[1] = "Forest Area"
    df_name.columns.values[2] = "CO2 Emmission"
    df_name.columns.values[3] = "Total Population"
    return (df_name)

def heatmap(country_name):
    """
    Creates a correlation heatmap for the country given as argument.
    Parameters
    ----------
    country_name : string
        Name of the country to create the heatmap for.
    Returns
    -------
    None.
    """

    # creates dataframe name
    df_name = "df_" + country_name
    # calls function to create dataframe
    df_name = country_df(country_name)
    # plots heatmap
    dataplot = sns.heatmap(df_name.corr(), cmap="Blues", annot=True, fmt='.3g')
    # saves figure
    filename = country_name + "_heatmap.png"
    plt.title(country_name, fontsize=15, fontweight='bold')
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
heatmap("China")
heatmap("United States")

def stat_pop():
    """
      Defining a statistical function for the population .
    ----------
    country_name : string
        Name of the country to create the heatmap for.
    Returns
    -------
    None.
    """
    df_Population_stat, df_Population_countries_stat = read_file(
    "population.xlsx")
    df_Population_stat = df_Population_stat[['1991', '1995', '2000', '2005',
                                             '2010']]
    
    print(df_Population_stat.describe())
    print("Pearsons correlations")
    print(df_Population_stat.corr())

    print("Kendall correlations")
    print(df_Population_stat.corr(method="kendall"))
    print("Average population\n", df_Population_stat.mean())
    print("Median population\n", df_Population_stat.median())
    # calculate the skewness,kurtosis and Covariance
    print("std. deviations:\n", df_Population_stat.std())
    print("skewness:\n", df_Population_stat.skew())
    print("kurtosis:\n", df_Population_stat.kurtosis())
    
# Reading the data files
stat_pop()









 
 
 
 
 
 
 
 
 
 
 
 
 

