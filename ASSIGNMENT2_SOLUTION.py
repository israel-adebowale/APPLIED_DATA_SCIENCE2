

#import important libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
excel_url_C02 = 'https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=excel'
# all the data used have the same sheet name
sheet_name = 'Data'
new_cols = ['Country Name', '2000', '2002', '2004', '2006','2008', '2010', '2012', '2014']
countries = ['Canada', 'United States', 'United Kingdom', 'Nigeria', 'China', 'Brazil', 'Australia']

#Each parameters are passed into the function to produced the preprocessed and transposed dataframe 

data_urban_read, data_urban_transpose = read_data_excel(excel_url_urban, sheet_name, new_cols, countries)
data_electricity_read, data_electricity_transpose = read_data_excel(excel_url_electricity, sheet_name, new_cols, countries)
data_agriculture_read, data_agriculture_transpose = read_data_excel(excel_url_agriculture, sheet_name, new_cols, countries)
data_C02, data_C02_transpose = read_data_excel(excel_url_C02, sheet_name, new_cols, countries)


print(data_urban_read)

print(data_urban_transpose)


print(data_electricity_read)


print(data_electricity_transpose)

print(data_agriculture_read)

print(data_agriculture_transpose)


print(data_C02 )


print(data_C02_transpose)



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
y_data = [data_electricity_transpose['Canada'], 
          data_electricity_transpose['United States'], 
          data_electricity_transpose['Nigeria'],
          data_electricity_transpose['China'], 
          data_electricity_transpose['Brazil'], 
          data_electricity_transpose['Australia']]
xlabel = 'Year'
ylabel = 'Countries'
labels = ['Canada', 'USA', 'UK', 'Nigeria', 'China', 'Brazil', 'Australia']
colors = ['red', 'magenta', 'blue', 'yellow', 'green', 'purple', 'black']
title = 'Electricity production from oil, gas and coal sources (% of total)'

# the attributes are passed into the function and returned to give the desired plot
multiple_plot(x_data, y_data, xlabel, ylabel, title, labels, colors) 



# parameters for producing multiple plots of CO2 emissions (metric tons per capita)
x_data = data_C02_transpose.index # the  row index is used as the values for the x-axis
y_data = [data_C02_transpose['Canada'], 
          data_C02_transpose['United States'], 
          data_C02_transpose['Nigeria'],
          data_C02_transpose['China'], 
          data_C02_transpose['Brazil'], 
          data_C02_transpose['Australia']]
xlabel = 'Year'
ylabel = 'Countries'
labels = ['Canada', 'USA', 'UK', 'Nigeria', 'China', 'Brazil', 'Australia']
colors = ['red', 'magenta', 'blue', 'yellow', 'green', 'purple', 'black']
title = 'CO2 emissions (metric tons per capita)'
# the attributes are passed into the function and returned to give the desired plot
multiple_plot(x_data, y_data, xlabel, ylabel, title, labels, colors)




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
    


    plt.legend()
    ax.tick_params(bottom=False, left=True)

    plt.show()



# the parameters for producing grouped bar plots of Urban population growth (annual %)
labels_array = ['Canada', 'USA', 'UK', 'Nigeria', 'China', 'Brazil', 'Australia']
width = 0.2 
y_data = [data_urban_read['2000'], 
          data_urban_read['2004'], 
          data_urban_read['2008'], 
          data_urban_read['2012']]
y_label = 'Urban growth'
label = ['Year 2000', 'Year 2004', 'Year 2008', 'Year 2012']
title = 'Urban population growth (annual %)'

# the parameters are passed into the defined function and produces the desired plot
barplot(labels_array, width, y_data, y_label, label, title)



# # the parameters for producing grouped bar plots of Agriculture, forestry, and fishing, value added (% of GDP)
labels_array = ['Canada', 'USA', 'UK', 'Nigeria', 'China', 'Brazil', 'Australia']
width = 0.2 
y_data = [data_agriculture_read['2000'], data_agriculture_read['2004'], data_agriculture_read['2008'], data_agriculture_read['2012']]
y_label = 'Agriculture'
label = ['Year 2000', 'Year 2004', 'Year 2008', 'Year 2012']
title = 'Agriculture, forestry, and fishing, value added (% of GDP)'

# the parameters are passed into the defined function and produces the desired plot
barplot(labels_array, width, y_data, y_label, label, title)

#Here we create a dataframe of Canada which takes some indicators as parameters
data_Canada = {'Urban pop. growth': data_urban_transpose['Canada'],
        'Electricity production': data_electricity_transpose['Canada'],
        'Agric. forestry and Fisheries': data_agriculture_transpose['Canada'],
        'CO2 Emmissions': data_CO2_transpose['Canada'],
        'Forest Area': data_forest_transpose['Canada'],
        'GDP Annual Growth': data_GDP_transpose['Canada']        
        }

df_Canada = pd.DataFrame(data_Canada)
print(df_Canada)



