#!/bin/python3

'''
Project Name: Python_Pandas_Learning
Date started: Dec 01, 2020
Author: Olga Lazarenko
Description: the purpose of the project is to get more familiar and 
             enhance skills at Pandas package:
             - work with series
             - work with DataFrame
             

'''
print("Started on Dec 02, 2020")

import pandas as pd
import numpy as np

#   ***** SERIES *****

# create series: pandas.Series( data, index, dtype, copy) 
# using (array, dict, scalar value/ or constant)

# create empty series
empty_series = pd.Series()
print(empty_series)
print()
print('lenth = ' + str(len(empty_series)))
print('****')
print()


#  ***  create a series from ndarray with default/or passed index
data_country = np.array(['Canada','USA','Germany','France','Italy']) # with the default indexes (starts with zero)
country_series = pd.Series(data_country)
print(country_series)
print()
print()

country_series_2 = pd.Series(data_country) # with the passed/customized indexes ( in this case, starts with 1)
print(country_series_2)
print()
print()

# **** create series from dict
np.iinfo(np.int32).max
np.iinfo(np.int64).max
country_capital_dict = {'Germany':'Berlin', 'US':'Washington',
                         'Italy':'Rome', 'France':'Paris',
                         'Russia':'Moscow','Spain':'Madrid',
                         'Austria':'Vienna','Greece':'Athens'}
country_capital_series = pd.Series(country_capital_dict)
print(country_capital_series)
print()
print()

country_capital_dict = {'Germany':'Berlin', 'US':'Washington',
                         'Italy':'Rome', 'France':'Paris',
                         }
country_capital_series = pd.Series(country_capital_dict)
print(country_capital_series)

#  (!)  to change index
country_capital_series.index = ['1','2','3','4']
print()
print(country_capital_series)
print()


# create a DataFrame using a single list
cars = ['Ford','Honda','Chevy','Nissan','Kia']
df_cars = pd.DataFrame(cars)
print('df_cars')
print(df_cars)
print()
print()

# cread a DataFrame using a list of lists
cars_details = {'Honda':['Civic','Accord','Acura','Pilot','Odyssey','Fit','Ringline', 'Civic Hatchback','HR-V'] ,
                 'Year':['2005','2012','2018','2020','2013','2019','2020','2019', '2014'] , 
                 'Mileage':[98600,55000,16000,126000,150000,17000,500,10000,110000] ,
                 'Price': [6500,12300,15500,18000,77000,16600,34000,19000,12000] ,
                 'Category': ['sedan','sedan','sedan','suv','minivan','hatchback','truck', 'hatchback','suv']
                 
                 }
df_cars_details = pd.DataFrame(cars_details)
print(df_cars_details)
print()
print('-----------------------------------')
print()
print(df_cars_details.loc[df_cars_details.Price <= 15000])

# try to change the index at df_cars_details
df_cars_details.index = ['1','2','3','4','5','6','7','8','9']
print('df_cars_details with new indexes')
print(df_cars_details)
print()
print('--------------------------------------')
print()
# assign series 
ser1 = pd.Series(['Mary','Smith','01/24/2000'])
ser2 = pd.Series(['Paul','Logan','03/15/1988'])
ser3 = pd.Series(['Lorna','Berrian','11/22/1999'])
# framing the series into data frame
df_employee = pd.DataFrame([ser1,ser2,ser3])
print(df_employee)
print()
 
'''
# change the index
df_employee.index = ['1','2','3']
print()
print(df_employee)
'''
# framing in another way, add the index and the columns name
df_employee.index = ['row1','row2','row3'] 
df_employee.columns = ['FirstName', 'LastName', 'DOB']
print(df_employee)
print()
print('*******')
# print the first row of the data frame df_employee
print('Data Frame df_empoyee, the first row')
print(df_employee.head(1))
print()
# print the first two row of the data frame df_cars_details
print('Data Frame df_cars_detail the first two rows')
print(df_cars_details.head(2))
print()
# print the first five rows
print('Data Frame df_cars_details, the first five rows ')
print(df_cars_details.head())
print()
print('Data Frame df_cars_details, without four last rows')
print(df_cars_details.head(-4))
print('------------')
print()
print('* Number of rows and columns of the DataFrames *')
print("DataFrame df_cars")
print(df_cars)
print(df_cars.shape)
print()
print()
print('DataFrame df_cars_details')
print(df_cars_details)
print(df_cars_details.shape)
print()
print()
print('DataFrame df_employee')
print(df_employee)
print(df_employee.shape)
print()
print()

# ***    Indexing the DataFrame using iloc[:,:] methond    ***
print('* Indexing the DataFrame, iloc method')
print('DataFrame df_cars_details') 
print(df_cars_details)
print()

# print the entire DataFrame
print('df.iloc[:,:] , the entire DataFrame is retrieved')
print(df_cars_details.iloc[:,:])
print()
print()

# print the first three rows and the first two columns
print('first 3 rows and first 2 columns')
print(df_cars_details.iloc[:3,:2])
print()
print()

# print rows starting from 2nd to 5th, and columns from 3rd to 4th
print('print rows from 2 to 5 and columns from 3 to 4')
print(df_cars_details.iloc[1:5,2:4]) 
# (!) started from the less index that is required to obtain 
print()
print()

print('print the last 2 rows of the DataFrame')
print(df_cars_details.iloc[-2:]) # or iloc[-2:,:]
print()
print()

# print the last 2 rows of the last column
print('last 2 rows for the last column')
print(df_cars_details.iloc[-2:,-1])
print()
print()

# use tail() methond to obtain last n rows
print('tail() method to obtain  last n rows')
print(df_cars_details.tail(1))
print()
print(df_cars_details.tail(3))
print()
print()

# Indexing the DataFrame by the rows/columns labels, using .loc[:,:] methond
# row/column label is row/column name
# let's look at the DataFrame df_cars_details
print(df_cars_details)
df_cars_details2 = df_cars_details.copy() # create the copy
print()
print('the copy')
print(df_cars_details2)
print()


df_cars_details2.index = [
                          'Row 1',
                          'Row 2',
                          'Row 3',
                          'Row 4',
                          'Row 5',
                          'Row 6',
                          'Row 7',
                          'Row 8',
                          'Row 9'
                        ]
print(df_cars_details2)
print()
print()

# now at the dataframe df_cars_details2 we retrieve the elements uning loc[] method
# elements from the Row 2 to Row 6 and from the column Mileage, Price

print(df_cars_details2.loc["Row 2" : "Row 6","Mileage" : "Price"])
# (!) I started from the required row, not one row ahead
print()
print()


#   ***   compute the summary statistics for the dataframe df_cars_details  ***
print('The summary statistics')
print(df_cars_details.describe())
print()
print()

#   *** compute the correlations ***
print('Correlations')
print(df_cars_details.corr())
print()
print()

#   *** compute numerical data ranks *** ???????
print('Numerical data ranks')
print(df_cars_details.rank())
print()
print()

# ***   Sorting the dataframe   ***
print('sort by year asc')
print(df_cars_details.sort_values(by = ["Year"], inplace = False)) 
# inplace = False, thus the copy of the dataframe is returned
print()
print('sort by year desc')
print(df_cars_details.sort_values(by = ["Year"], inplace = False, ascending = False))