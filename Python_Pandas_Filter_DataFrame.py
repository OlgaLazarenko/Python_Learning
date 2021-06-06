# Filter DataFrame
#!/bin/python3


import pandas as pd

# create <auto> DataFrame by reading the data file
auto = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv" , 
                  usecols = ['Make' ,
                              'Normalized Loss',
                              'Symboling',
                              'Body Style' , 
                              'City mpg' ,
                              'Highway mpg',  
                              'Price'])

print()
print("<auto> DataFrame")
print(auto.head())

# drop empty rows
auto.dropna()

auto["Make"] = auto["Make"].str
auto["Body Style"] = auto["Body Style"].str
print(auto.dtypes)

'''
# 1) Filter the data, DataFrame way
new_auto1_toyota = auto[auto["Make"] == "toyota"]
print()
print("<new_auto1_toyota>  DataFrame")
print(new_auto1_toyota)
print()
print()
bmw_volvo = auto[ (auto["Make"] == "bmw") & (auto["Make"] == "volvo")]
print("bmw_volvo>  DataFrame")
print(bmw_volvo)
'''

# <Empty DatFrame> notification is returned 
# check the columns data type

# convert <Make> column data type from object to string
# change the columns data types to appropirate ones



