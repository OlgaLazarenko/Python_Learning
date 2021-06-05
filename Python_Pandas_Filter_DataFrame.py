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

# 1) Filter the data, DataFrame way
new_auto1_toyota = auto[auto["Make"] == "toyota"]
print()
print("<new_auto1_toyota>  DataFrame")
print(new_auto1_toyota)
print()
print()
new_auto1_bmw_volvo = auto[ (auto["Make"] == "bmw") & (auto["Make"] == "volvo")]
print("<new_auto1_bmw_volvo>  DataFrame")
print(new_auto1_bmw_volvo)

# <Empty DatFrame> notification is returned 
# check the columns data type
print("columns data type")
print(auto.dtypes)
print()
print()
# convert <Make> column data type from object to string
# change the columns data types to appropirate ones
convert_dict = {"Symboling" : str , 
                "Normalized Loss" : int ,
                "Make" : str ,
                "Body Style" : str ,
                "City mpg" : int ,
                "Highway" : int , 
                "Price" : int}

auto = auto.astype(convert_dict)

print("converted  data type")
print(auto.dtypes)