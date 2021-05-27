# Axes Operations at DataFrames
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

# create  <auto_part1> subset DataFrame by selecting the desired columns from <auto> DataFrame
print()

auto_part1 = auto[["Make" , "City mpg" , "Highway mpg"]]
print("auto_part1")
print(auto_part1)


