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

# create a DataFrame using a single list/ or list of lists
cars_list = ['Ford','Honda','Chevy','Nissan','Kia']
df_cars = pd.DataFrame(cars_list)
print('df_cars')
print(df_cars)