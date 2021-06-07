# Filter DataFrame
#!/bin/python3


import pandas as pd
import numpy as np

# create <auto> DataFrame by reading the data file
auto = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv" , 
                  usecols = ['Make' ,
                              'Normalized Loss' ,
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

# ****   1) Filter the data, DataFrame way
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
print()
print('-----------------------------------------------')

# --------------------------------------------------------------------------------------------------------

# ****  2) Filter the data, Query Function
honda_df = auto.query('Make == "honda"')
print()
print("<new_volvo>  DataFrame")
print(honda_df)
print("number of rows" + str(len(honda_df)))
print()

# convert <Price> column from object data type to int data type
honda_df["Price"] = honda_df["Price"].astype(float)
print(honda_df.dtypes)
print()
# mention value explicitly 
honda_df2 = auto.query('Make == "honda" & Symboling == "2"')
print("<honda_df2>  DataFrame")
print(honda_df2)
print()

# reference method 
my_val = 'toyota'

toyota_df = auto.query("Make == @my_val")
print("<toyota_df>  DataFrame")
print(toyota_df)
print()

my_symb = 2
toyota_df2 = auto.query("Make == @my_val  & Symboling == @my_symb")
print("<toyota_df2>  DataFrame")
print(toyota_df2)
print()

# pass colunm name as a varible in query
my_var = 'Symboling'
my_var2 = 'Make'
sedan_df = auto.query( "{0} == '3'".format(my_var) )
print("<sedan_df>   DataFrame, the column name is passed in the query as a variable")
print(sedan_df)




