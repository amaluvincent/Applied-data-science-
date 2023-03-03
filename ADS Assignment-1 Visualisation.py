# -*- coding: utf-8 -*-

"""
This code Plots 3 different visualisation method (line grap, pie chart,
stacked bar plot) from 3 different data set .

"""
# Importing required packages
import pandas as pd
import matplotlib.pyplot as plt

# Function to plot line graph.
def line_plot(wood):
    """
    
    This function will plot line graph of apparent wood consumption   
    in UK from 1999-2017.Graphs are also saved as images to local directory.

    Parameters
    ----------
     wood : This is a DataFrame used to plot line graph.
         This line graph depicts the Apparent consumption of wood which is 
         the sum of UK production,Imports, and Exports from 1999-2017.
     
     Returns
    -------
    None.

    """
    plt.figure()
    plt.plot(wood["year"], wood["UK production"], 
             label="UK production")
    plt.plot(wood["year"], wood["Imports"], label="Imports")
    plt.plot(wood["year"], wood["Exports"], label="Exports")
    plt.plot(wood["year"], wood["Apparent Consumption"],
             label="Apparent Consumption")
   
    # Set title and labels 
    plt.xlabel("Year")
    plt.ylabel("Million m3 WRME underbark  ")
    plt.title("Apparent consumption of wood in the UK, 1999-2017")
    
    # Removing white space from left and right.
    plt.xlim(2008, 2017)
    
    # plot the graph  with labels.
    plt.legend()
    plt.savefig('lineplot.png')
    plt.show()
    
# Reading the file to the dataframe 'wood' 
wood= pd.read_excel("apparent_consumption_of_wood.xlsx")
line_plot(wood)

# Function to plot pie chart.
def pie_plt(infant):
    """
    
    This function will plot pie chart of infant mortality rate of seven 
    different countries in 2023.Graphs are also saved as images to 
    local directory.

    Parameters
    ----------
    infant : This is a DataFrame used to plot pie chart. 
        This pie chart will do the comparison of Infant mortality of 7 
        different countries in 2023 .
        

    Returns
    -------
    None.

    """
    
    
    
    plt.figure()
    plt.pie(infant['Infant Mortality Rate'], labels=infant['country'], 
        autopct='%1.1f%%', pctdistance=0.7, labeldistance=1.1,
        wedgeprops={'linewidth' : 1.0, 'edgecolor' : 'white'} )
    
    # Set title and show the figure
    plt.title("Infant Mortality Rate in 2023")
    plt.savefig('pieplot.png')
    plt.show()
    
# Reading the file into dataframe 'infant'    
infant = pd.read_excel("2023_infant_mortality_rate.xlsx")    
pie_plt(infant)

# Function to plot stacked bar plot.
def bar_plot(paper):
    """
    This function will plot stacked bar plot of UK paper production   
    from 2015 - 2019.Graphs are also saved as images to local directory.

    Parameters
    ----------
    paper : This is a DataFrame used to plot stacked bar plot.
        This stacked bar plot shows the different type of paper production in
        UK from the period 2015-2019 .

    Returns
    -------
    None.

    """
    
    
    plt.figure()
    # Calling functions to create plots.
    paper.plot(x='Year', kind='bar', stacked=False)
    
    # Set title and labels.
    plt.title('Uk paper production 2015-2019')
    plt.ylabel("production (thousand tonnes)") 
    plt.savefig('stackedplot.png')
    plt.show()
    
# Reading the file to the dataframe 'paper'.   
paper = pd.read_excel("production_of_paper.xlsx")
bar_plot(paper)    










