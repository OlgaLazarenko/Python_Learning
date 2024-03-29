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
print()

# select a subset of <auto_volvo>
auto_volvo_1 = auto_volvo[["Make" , "Body Style" ]]
print('auto_volvo_1')
print(auto_volvo_1)
print()
4
auto_volvo_2 = auto_volvo[["Symboling" , "Normalized Loss" , "City mpg" , "Highway mpg" , "Price"]]
print()
print("auto_volvo_2")
print(auto_volvo_2)
print()

# combine the dataframes <auto_volvo_1> and <auto_volvo_2), axis = 1
volvo_result_ax1 = pd.concat([auto_volvo_1, auto_volvo_2], axis = 1)
print('concatenated dataframes , axis=1')
print(volvo_result_ax1)
print()

# combine the dataframes, axis = 0
volvo_result_ax2 = pd.concat([auto_volvo_1, auto_volvo_2] , axis= 0)
print('concatenated dataframes , axis=0')
print(volvo_result_ax2)

# create <auto_porshe> dataframe
auto_bmw = auto[auto["Make"] == "bmw"]
print("<auto_bmw> dataframe")
print(auto_bmw)

# concatenate <auto_bmw> and <auto_volvo> dataframes
auto_bmw_volvo = pd.concat([auto_bmw , auto_volvo])
print("<auto_bmw_volvo>  dataframe")
print(auto_bmw_volvo)
print()
print()

# create series
bmw_sr = pd.Series(["high","low","low","low","moderate","low","low","low"])
print("<bmw_sr> created series")
print(bmw_sr)
print()
print(auto_bmw)
# concatentate <auto_bmw> dataframe and <bmw_sr> series ???????
bmw_df_sr = pd.concat([auto_bmw , bmw_sr] , axis = 1 )
print('concatenate datframe and series, <bmw_df_sr>')
print(bmw_df_sr)

# concatenate series
sr_ID = pd.Series(["0001","0002","0003","0004","0005"] , name = "Car ID")
sr_make = pd.Series(["volvo","bmw","honda","toyota","ford"] , name = "Producer")
sr_style = pd.Series(["sedan","couple","wagon","convertible","truck"] , name = "Type")

#create dataframe <my_auto> from the series
my_auto = pd.concat([sr_ID , sr_make , sr_style] , axis = 1 )
print()
print("<my_auto> dataframe")
print(my_auto)

# override the existing columns
my_auto = pd.concat([sr_ID , sr_make , sr_style] , axis = 1 , keys = ["CarID" , "Make" , "BodyStyle"])
print()
print(my_auto)

# override the indexes
my_auto