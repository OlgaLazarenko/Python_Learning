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

print()
print("auto DataFrame shape:")
print(auto.shape)

# create  <auto_part1> subset DataFrame by selecting the desired columns from <auto> DataFrame
print()

auto_part1 = auto[["Make" , "City mpg" , "Highway mpg"]]
print('auto_part1 DataFrame shape')
print(auto_part1.shape)

# ------------------------------------------------------------

# Operations on Axes of DataFrame

print()
print("average mileage City/Highway (axis = 0, axis = 'row') ")
print(auto_part1.mean(axis = 0)) # the agv value is calculated for each column ('City mpg', 'Highway mgp')
print()
print()
print("average mileage City/Highway (axis = 1, axis = 'column') ")
print(auto_part1.mean(axis = 1)) # the avg value is calculated for each row
print()
print()
print("max mileage City/Highway (axis = 0)")
print(auto_part1.max(axis=0))
print()
print()
print("max mileage City/Highway (axis = 1) ")
print(auto_part1.max(axis=1))
print()
print()
print("min mileage City/Highway (axis = 0)")
print(auto_part1.min(axis=0))
print()
print()
print("min mileage City/Highway (axis = 1) ")
print(auto_part1.min(axis=1))
print()

# create a subset of the initial dataframe
print("<auto_volvo> dataframe")
auto_volvo = auto[auto["Make"] == 'volvo']
print(auto_volvo)
# resent the indexes of <auto_volvo> dataframe
auto_volvo.reset_index(drop = True)
print()
print('new indexes')
print(auto_volvo)
