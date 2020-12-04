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

# create a DataFrame using a single list
cars = ['Ford','Honda','Chevy','Nissan','Kia']
df_cars = pd.DataFrame(cars)
print('df_cars')
print(df_cars)
print()
print()

# cread a DataFrame using a list of lists
cars_details = {'Honda':['Civic','Accord','Avalon','Pilot','Odyssey','Fit'] ,
                 'Year':['2005','2012','2018','2020','2013','2019'] , 
                 'Mileage':['98600','55000','16000','126000','150000','17000']}
df_cars_details = pd.DataFrame(cars_details)
print('df_cars_details')
print(df_cars_details)