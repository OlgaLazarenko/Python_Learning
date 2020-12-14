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
ser1 = pd.Series('Mary','Smith','01/24/2000')
ser2 = pd.Series('Paul','Logan','03/15/1988')
ser3 = pd.Series('Lorna','Berrian','11/22/1999')
# framing the series into data frame
df_employee = pd.DataFrame([ser1,ser2,ser3])
print(df_employee)


