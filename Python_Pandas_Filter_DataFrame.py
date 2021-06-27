# Filter DataFrame
#!/bin/python3


import pandas as pd
import numpy as np
import random

# create <auto> DataFrame by reading the data file
auto = pd.read_csv("E:/_Python_Projects_Data/Data_Visualization/Autos_Data_Set/Car_Import_1985.csv" )


print()
lenght_auto_df = len(auto)
print("lenght <auto> data frame")
print(lenght_auto_df)
print()

print(' --- Columns of <auto> data frame:')
for col in auto.columns:
    print(col)
print()
print()

auto.rename(columns = {'' : 'Index'} , inplace = True)

print(' --- Columns of <auto> data frame:')
for col in auto.columns:
    print(col)
print()
print()

# generate a list of random numbers as invoice numbers
invoice_list = []
invoice_list = random.sample(range(7000,9999) , 205 )

# insert the list <invoice_list> as a new column "Invoice" at the data frame <auto>
auto.insert(0, "Invoice" , invoice_list , True)

print(' ---- New column "Invoice" is inserted: ')
for col in auto.columns:
    print(col)


print()
print("<auto> DataFrame")
print(auto)
print('--------------------------------------------------')
print()
print(auto.dtypes)


# replace '?' in the columns 'Price' with 0
auto['Price'] = np.where(auto['Price'] == '?' , '0', auto['Price'] )
print('******')
print(auto.dtypes)
print()
auto['Price'] = auto['Price'].astype(int)
auto['Normalized Loss'] = np.where(auto['Normalized Loss'] == '?' , '0', auto['Price'] )
auto['Normalized Loss'] = auto['Normalized Loss'].astype(int)
print()
print(auto.dtypes)
'''

# number of rows in the initial <auto> DataFrame
index = auto.index
numb_of_rows =  len(index)
print()
print('* the initial number of rows ' + str(numb_of_rows))
print()
print('---------------------------------------------------')
print('NaN values')
print(auto.isnull().values.any())
print('---------------------------------------------------')

auto.replace(np.nan , 0 )
auto.replace(['?'],'0')

# drop empty rows
auto.dropna()
print()
print('* NaN values are removed, the number of rows: ' + str(len(auto))  )
print()

# iterate over indices
print('indices')
for row in auto.index:
    print(row , end = " ")

# -----------------------------------------------------------------------------------


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

# -------------------------------------------------------------------------------

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
toyota_df2 = auto.query("Make == @my_val  & Symboling == @my_symb") # multiple conditions
print("<toyota_df2>  DataFrame")
print(toyota_df2)
print()

# pass colunm name as a varible in query
my_var = 'Make'
sedan_df = auto.query( "{0} == 'sedan'".format(my_var) )
print("<sedan_df>   DataFrame, the column name is passed in the query as a variable")
print(sedan_df) # >??????? 
print()
# ---------------------------------------------------------------------------------------------

# ****  3) Use <loc> function to filter data frame
# use <bmw_volvo> data frame
print('bmw_volvo  DataFrame')
print(bmw_volvo)
print()
print('indexes')
print(bmw_volvo.index)
print()
# sort by the column "Price" desc way
# inpalce = False/True --------------------------------
# --- inplace = False (defaut option)
bmw_volvo.sort_values( by =['Price'] , ascending = False , inplace = False) # default <inplace>
print('sorted bmw_volvo , inplace = False')
print(bmw_volvo) # the initial <bmw_volvo> data frame is not changed
print()
sorted_bmw_volvo = bmw_volvo.sort_values( by =['Price'] , ascending = False , inplace = False)
print("new df")
print(sorted_bmw_volvo)
print()
print()
# --- inplace = True ----------------------------------
bmw_volvo2 = bmw_volvo # create a copy of bmw_volvo data frame, in oder to keep it untouched
bmw_volvo2.sort_values( by = ['Price'], ascending = False , inplace = True)
print("sorted , inplace = True")
print(bmw_volvo2) # the data frame <bmw_volvo2> was modified/updated after sorting 
print()
print()


# rename columns
auto.rename( columns = {'Normalized Loss':'Normalized_Loss' , 'Body Style':'Body_Style'} , inplace = True)

auto_toyota_sedan = auto.loc[((auto['Make']=='toyota') & (auto['Body_Style']=='sedan') & (auto['Price'] >= 10000))]
print()
auto_toyota =  auto.loc[ (auto['Make']=='toyota') ]
print("<auto_toyota>  data frame")
print(auto_toyota)
print()
print()
print("<auto_toyota_sedan>  DataFrame")
print(auto_toyota_sedan)
print(auto.dtypes)
print()

# sort <auto_toyota> data frame
toyota_sorted = auto_toyota.sort_values( by = ['Price'] , ascending = False , inplace = False)
print('<toyota_sorted>  data frame')
print(toyota_sorted)
print()

# --- iloc filtering -----------------------------------------------
# 5 most expensive imported Toyota cars
toyota_5max_price = toyota_sorted.iloc[0:5]
print(" 5 most expensive imported Toyota cars")
print(toyota_5max_price)
print()

# 10 most expensive imported Toyota cars
toyota_10max_price = toyota_sorted.iloc[0:10]
print("10 most expesive imported Toyota cars")
print(toyota_10max_price)
print()
# 5 most cheapes Toyota cars
toyota_len = len(toyota_sorted)
toyota_5min_price = toyota_sorted.iloc[(toyota_len - 5): (toyota_len)]
print("5 cheapest imported Toyota ")
print(toyota_5min_price)



new_sorted_bmw_volvo = bmw_volvo.sort_values( by =['Price'] , ascending = False , inplace = False) # default <inplace>
print('sorted bmw_volvo, inplace = False, asigned to new data frame')
print(new_sorted_bmw_volvo) # sorted data frame is returned the initial data frame <bmw_volvo> is not changed
print()

print(bmw_volvo)
'''










