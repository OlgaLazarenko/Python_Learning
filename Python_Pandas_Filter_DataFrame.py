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
new_auto_1 = auto[auto["Make"] == "toyota"]
print()
print("<new_auto_1>  DataFrame")
print(new_auto_1)