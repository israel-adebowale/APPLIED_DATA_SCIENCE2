# import important libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# define functions for reading and transposing data
def read_data_excel(excel_url, sheet_name, new_cols, countries):
    """
    This function defines all the necessary attributes for reading the excel files,
    preprocessing and transposing it.
    excel_url depicts the downloaded link of the file,
    sheet_name states the name of the excel sheet
    new_cols are the newly created columns for the visualization
    Lastly, countries are the selected countries for the visualization.
    The tranpose function is used for transposing the preprocessed data
    """
    data_read = pd.read_excel(excel_url, sheet_name=sheet_name, skiprows=3) # the first 3 rows of the data are skipped
    data_read = data_read[new_cols] # a new column is produced for the read data 
    data_read.set_index('Country Name', inplace=True) # the index of the newly created dataframe is set and named.
    data_read = data_read.loc[countries] # the loc keywords brings out the location of the desired columns
    
    return data_read, data_read.T # the preprocessed data and transposed data are returned respectively.

# The excel url below indicates Urban population growth (annual %) 
excel_url_urban = 'https://api.worldbank.org/v2/en/indicator/SP.URB.GROW?downloadformat=excel' 

# The excel url below indicates electricity production from oil, gas and coal sources (% of total)
excel_url_electricity = 'https://api.worldbank.org/v2/en/indicator/EG.ELC.FOSL.ZS?downloadformat=excel'

# the excel url below indicates Agriculture, forestry, and fishing, value added (% of GDP)
excel_url_agriculture = 'https://api.worldbank.org/v2/en/indicator/NV.AGR.TOTL.ZS?downloadformat=excel'

# the excel url below indicates CO2 emissions (metric tons per capita)
excel_url_CO2 = 'https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=excel'

# the excel url below indicates Forest area (% of land area)
excel_url_forest = 'https://api.worldbank.org/v2/en/indicator/AG.LND.FRST.ZS?downloadformat=excel'

# the excel url below indicates GDP growth (annual %)
excel_url_GDP = 'https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel'

# all the data used have the same sheet name
sheet_name = 'Data'
new_cols = ['Country Name', '1997', '2000', '2003', '2006','2009', '2012', '2015']
countries = ['Germany', 'United States', 'United Kingdom', 'Nigeria', 'China', 'Brazil', 'Australia']

# Each parameters are passed into the function to produced the preprocessed and transposed dataframe 
data_urban_read, data_urban_transpose = read_data_excel(excel_url_urban, sheet_name, new_cols, countries)
data_electricity_read, data_electricity_transpose = read_data_excel(excel_url_electricity, sheet_name, new_cols, countries)
data_agriculture_read, data_agriculture_transpose = read_data_excel(excel_url_agriculture, sheet_name, new_cols, countries)
data_CO2, data_CO2_transpose = read_data_excel(excel_url_CO2, sheet_name, new_cols, countries)
data_forest, data_forest_transpose = read_data_excel(excel_url_forest, sheet_name, new_cols, countries)
data_GDP, data_GDP_transpose = read_data_excel(excel_url_GDP, sheet_name, new_cols, countries)


#Each of the preprocessed and transpose dataframes are printed below
print(data_urban_read)

print(data_urban_transpose)

print(data_electricity_read)

print(data_electricity_transpose)

print(data_agriculture_read)

print(data_agriculture_transpose)

print(data_CO2 )

print(data_CO2_transpose)

print(data_forest)

print(data_forest_transpose)

print(data_GDP)

print(data_GDP_transpose)

# the descriptive statistics of GDP growth (annual %) which takes the countries as columns and year as index are described below
GDP_statistics = data_GDP_transpose.describe()
print(GDP_statistics)

# the desciptive statistics of Forest area (% of land area)
forest_statistics = data_forest_transpose.describe()
print(forest_statistics)

# The function below construct a multiple line plot
def multiple_plot(x_data, y_data, xlabel, ylabel, title, labels, colors):
    """
    This function defines a mutiple line plots which attributes are discussed below:
    x_data: states the index which represent the years of the indicators
    y_data: states the countries of the indicators
    xlabel: depicts the label of the x-axis
    ylabel: depicts the y-axis label
    title: shows the title if the plot
    labels: these are the specific labels of each line plots which is displayed by the legend function
    colors: these are the colors of each line plots on the graph
    """
    plt.figure(figsize=(12,8)) 
    plt.title(title, fontsize=20) 
    for i in range(len(y_data)):  # this loops over the dataframe and produces the desired plot
        plt.plot(x_data, y_data[i], label=labels[i], color=colors[i])
    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    plt.legend(bbox_to_anchor = (1.02,1))
    plt.show()
    return


# Parameters for plotting multiple line plots of electricity production from oil, gas and coal (% of total)
x_data = data_electricity_transpose.index # the  row index is used as the values for the x-axis
y_data = [data_electricity_transpose['Germany'], 
          data_electricity_transpose['United States'], 
          data_electricity_transpose['Nigeria'],
          data_electricity_transpose['China'], 
          data_electricity_transpose['Brazil'], 
          data_electricity_transpose['Australia']]
xlabel = 'Year'
ylabel = '% electricity production'
labels = ['Germany', 'USA', 'UK', 'Nigeria', 'China', 'Brazil', 'Australia']
colors = ['red', 'magenta', 'blue', 'yellow', 'green', 'purple', 'black']
title = 'Electricity production from oil, gas and coal sources (% of total)'

# the attributes are passed into the function and returned to give the desired plot
multiple_plot(x_data, y_data, xlabel, ylabel, title, labels, colors) 


# parameters for producing multiple plots of CO2 emissions (metric tons per capita)
x_data = data_CO2_transpose.index # the  row index is used as the values for the x-axis
y_data = [data_CO2_transpose['Germany'], 
          data_CO2_transpose['United States'], 
          data_CO2_transpose['Nigeria'],
          data_CO2_transpose['China'], 
          data_CO2_transpose['Brazil'], 
          data_CO2_transpose['Australia']]
xlabel = 'Year'
ylabel = 'metric tons'
labels = ['Germany', 'USA', 'UK', 'Nigeria', 'China', 'Brazil', 'Australia']
colors = ['red', 'magenta', 'blue', 'yellow', 'green', 'purple', 'black']
title = 'CO2 emissions (metric tons per capita)'

# the attributes are passed into the function and returned to give the desired plot
multiple_plot(x_data, y_data, xlabel, ylabel, title, labels, colors)

# The function below constructs a bar plot
def barplot(labels_array, width, y_data, y_label, label, title):
    """
    This function defines a grouped bar plot and it takes the following attributes:
    labels_array: these are the labels of barplots of the x-axis which depicts countries of the indicator to be determined
    width: this is the size of the bar
    y_data: these are the data to be plotted
    y_label: this is the label of the y-axis
    label: these are the labels of each grouped plots which depicts the years of the indicator 
    title: depicts the title of the bar plot.
    """
    
    x = np.arange(len(labels_array)) # x is the range of values using the length of the label_array
    fig, ax  = plt.subplots(figsize=(16,12))
    
    plt.bar(x - width, y_data[0], width, label=label[0]) 
    plt.bar(x, y_data[1], width, label=label[1])
    plt.bar(x + width, y_data[2], width, label=label[2])
    plt.bar(x + width*2, y_data[3], width, label=label[3])
    
    
    plt.title(title, fontsize=20)
    plt.ylabel(y_label, fontsize=20)
    plt.xlabel(None)
    plt.xticks(x, labels_array)
    
    sns.despine(bottom=True) #seaborn function despine is used to take away the top and the right spine of the function  #seaborn function despine is used to take away the top and the right spine of the function

    plt.legend()
    ax.tick_params(bottom=False, left=True)

    plt.show()
    return
    

# the parameters for producing grouped bar plots of Urban population growth (annual %)
labels_array = ['Germany', 'USA', 'UK', 'Nigeria', 'China', 'Brazil', 'Australia']
width = 0.2 
y_data = [data_urban_read['1997'], 
          data_urban_read['2003'], 
          data_urban_read['2009'], 
          data_urban_read['2015']]
y_label = 'Urban growth'
label = ['Year 1997', 'Year 2003', 'Year 2009', 'Year 2015']
title = 'Urban population growth (annual %)'

# the parameters are passed into the defined function and produces the desired plot
barplot(labels_array, width, y_data, y_label, label, title)


# the parameters for producing grouped bar plots of Agriculture, forestry, and fishing, value added (% of GDP)
labels_array = ['Canada', 'USA', 'UK', 'Nigeria', 'China', 'Brazil', 'Australia']
width = 0.2 
y_data = [data_agriculture_read['1997'], 
          data_agriculture_read['2003'], 
          data_agriculture_read['2009'], 
          data_agriculture_read['2015']]
y_label = '% of GDP'
label = ['Year 1997', 'Year 2003', 'Year 2009', 'Year 2015']
title = 'Agriculture, forestry, and fishing, value added (% of GDP)'

# the parameters are passed into the defined function and produces the desired plot
barplot(labels_array, width, y_data, y_label, label, title)


# Here I create a dataframe of Germany which takes some indicators as parameters
data_Germany = {'Urban pop. growth': data_urban_transpose['Germany'],
        'Electricity production': data_electricity_transpose['Germany'],
        'Agric. forestry and Fisheries': data_agriculture_transpose['Germany'],
        'CO2 Emmissions': data_CO2_transpose['Germany'],
        'Forest Area': data_forest_transpose['Germany'],
        'GDP Annual Growth': data_GDP_transpose['Germany']        
        }

# Here I create a dataframe of Nigeria which takes some indicators as parameters
data_Nigeria = {'Urban pop. growth': data_urban_transpose['Nigeria'],
        'Electricity production': data_electricity_transpose['Nigeria'],
        'Agric. forestry and Fisheries': data_agriculture_transpose['Nigeria'],
        'CO2 Emmissions': data_CO2_transpose['Nigeria'],
        'Forest Area': data_forest_transpose['Nigeria'],
        'GDP Annual Growth': data_GDP_transpose['Nigeria']        
        }

df_Germany = pd.DataFrame(data_Germany) # the desired columns are created using the pandas dataframe function
print(df_Germany)

df_Nigeria = pd.DataFrame(data_Nigeria)
print(df_Nigeria)

# The function below constructs a correlation dataframe using the scipy package
def correlation_pvalues(data_x, data_y):
    """
    This function defines correlation and pvalues of a particular indicator against other selected indicators
    data_x: the indicator of which we want to discuss
    data_y: the selected indicators from the dataframe
    """
    corr_dataframe = pd.DataFrame(columns=['r','p']) # r signifies correlation coefficient and p signifies p-values
    for col in data_y:
        if pd.api.types.is_numeric_dtype(data_y[col]) and not '': # it ignores anything that is not numeric
            r, p = stats.pearsonr(data_x, data_y[col]) # the scipy function used here for calculation the correlation coefficient and p-values
            corr_dataframe.loc[col] = [round(r,3), round(p,3)] # the values are round to 3 significant figures
    return corr_dataframe


# the indicator of interest is Urban population growth against the other factors from the Germany dataframe  
data_x = df_Germany['Urban pop. growth']
data_y = df_Germany

urban_pop_growth = correlation_pvalues(data_x, data_y) # the correlation coefficient and p values of Urban population growth against other indicators are printed below
print(urban_pop_growth)


# the indicator of interest is forest area against the other factors from the Germany dataframe  
data_x = df_Germany['Forest Area']
data_y = df_Germany

forest_area = correlation_pvalues(data_x, data_y) # the correlation coefficient and p values of Forest area against other indicators are printed below
print(forest_area)


# Here the correlation matrix of indicators for Germany are displayed below and it is used to construct the heatmap
corr_ger = df_Germany.corr()
print(corr_ger)

# The function below constructs a heatmap using the seaborn package
def heatmap(corr_matrix, title):
    """ This function defines a heatmap that accept the correlation matrix and title of the map as parameters """
    plt.figure(figsize=(7,7))
    sns.set(font_scale=1.0)
    sns.heatmap(corr_matrix, annot=True) # seaborn is used to produce the heatmap of the Germany indicators
    plt.title(title, fontsize=22)
    return

# the heatmap for germany is plotted below
heatmap(corr_ger, 'Germany') # the parameters are passed into the function and it is displayed below


# Here the correlation matrix of indicators for Nigeria are displayed below and it is used to construct the heatmap
corr_Nigeria = df_Nigeria.corr()
print(corr_Nigeria)

#the heatmap for Nigeria is plotted below
heatmap(corr_Nigeria, 'Nigeria') # the parameters are passed into the function and it is displayed below
