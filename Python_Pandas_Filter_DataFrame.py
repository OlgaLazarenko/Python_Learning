# Filter DataFrame
#!/bin/python3


import pandas as pd
import numpy as np

# create <auto> DataFrame by reading the data file
auto = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv" , 
                  usecols = ['Make' ,
                              'Symboling',
                              'Body Style' , 
                              'City mpg' ,
                              'Highway mpg',  
                              'Price'])

print()
print("<auto> DataFrame")
print(auto)
print()

# number of rows in the initial <auto> DataFrame
index = auto.index
numb_of_rows =  len(index)
print("number of rows")
print(numb_of_rows)
print()
print('------------------------------')
print('NaN values')
print(auto.isnull().values.any())
print('------------------------------')

auto.replace(np.nan , 0 )

print(auto)
# drop empty rows
print(auto)
auto.dropna()
new_index = auto.index
new_rows = len(new_index)
print("new number of rows")
print(new_rows)
print()

print("New data types")
print(auto.dtypes)

# 1) Filter the data, DataFrame way
new_auto1_toyota = auto[auto["Make"] == "toyota"]
print()
print("<new_auto1_toyota>  DataFrame")
print(new_auto1_toyota)
print()
print()
bmw_volvo = auto[ (auto["Make"] == "bmw") | (auto["Make"] == "volvo")]
print("bmw_volvo>  DataFrame")
print(bmw_volvo)
# number of rows
print("number of rows")
print(len(bmw_volvo))
print()
print()

# select data with hight mileage: city mpg >= 20, highway  mpg >=25
bmw_volvo_high_mpg = bmw_volvo[ (bmw_volvo["Make"] == "bmw") | (bmw_volvo["Make"] == "volvo") &
                                 (  (bmw_volvo["City mpg"] >= 20) & (bmw_volvo["Highway mpg"] >= 25))]

print("<bmw_volvo_high_mpg>  DataFrame") 
print(bmw_volvo_high_mpg)
# number of rows
print("number of rows")
print(len(bmw_volvo_high_mpg))
# <Empty DatFrame> notification is returned 
# check the columns data type

# convert <Make> column data type from object to string
# change the columns data types to appropirate ones
