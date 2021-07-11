# Filter DataFrame
#!/bin/python3


import pandas as pd
import numpy as np
import random

# create <auto> DataFrame by reading the data file
auto = pd.read_csv("E:/_Python_Projects_Data/Data_Visualization/Autos_Data_Set/Car_Import_1985.csv" )

print(auto.head())
# columns 
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
print()
print(auto.head(15))
print()
print('--- column data types')
print(auto.dtypes)
print()


# replace '?' in the columns 'Price' with 0
auto['Price'] = np.where(auto['Price'] == '?' , '0', auto['Price'] )
# convert the column 'Price' to integer data type
auto['Price'] = auto['Price'].astype(int)

# replace '?' at the column "Normalized_Loss" with 0
auto['Normalized_Loss'] = np.where(auto['Normalized_Loss'] == '?' , '0', auto['Normalized_Loss'] )
# convert the column 'Normalized_Loss' to integer data type
auto['Normalized_Loss'] = auto['Normalized_Loss'].astype(int)
print()
print(auto.dtypes)


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

auto.replace(np.nan , 0 ) # suppose it did't work ????
auto.replace(['?'],'0')

# drop empty rows
auto.dropna()
print()
print('* NaN values are removed, the number of rows: ' + str(len(auto))  ) # was this effective ????
print()
print(auto)


# drop '0' values of the column 'Normalized_Loss'
auto_loss = auto[auto['Normalized_Loss'] > 0]
print()
print(' --- <auto_loss>  data frame')
print(auto_loss)

print()
print(' max Normalized_Loss')
print(auto_loss['Normalized_Loss'].max())
print()

print(' min Normalized_Loss')
print(auto_loss['Normalized_Loss'].min())

auto_loss_sort_asc = auto_loss.sort_values( by = 'Normalized_Loss' , ascending = True , inplace = False)
print()
print(' --- auto_loss_sorted')
print(auto_loss_sort_asc)

# retrieve the first 12 rows with  minimal 'Normalized_Loss' / the ROWS POSITION
print(' -- 12 imported cars with min normalized loss:')
print(auto_loss_sort_asc.iloc[:12])
print()
print()
#retrieve the last 10 rows with maximum 'Normalized_Loss'/ the ROWS POSITION
print(' --  10 imported cars with max normalized loss:')
print(auto_loss_sort_asc.iloc[-10:])
print()
print()
# retrieve the invoice number of the first 12 cars with min normalized loss
print(auto_loss_sort_asc.iloc[:12 , 0])

# retrive the rows with indexes from 20 to 30 from <auto> data frame
print()
print('rows with indexes from 20 to 30:')
print(auto.loc[20:30])

# retrieve rows with indexes from 100 to 125 and the first three columns
print('rows with indexes from 100 to 125 and the first three columns')
# print(auto.loc[100:125 , 1:3])  ----   error generated !!!!
print(auto.iloc[120:125 , 1:3])

# print rows with indexes 10 to 22 and the columns from 5th column
print('rrows with indexes 10 to 22 and the columns from 5th column')
print(auto.iloc[10:22 , 5: ])


# print rows with indexes 10 to 25 and last 5 columns
print('rows with indexes 10 to 22 and last 5 columns')
print(auto.iloc[10:25 , -3:])
print()

# select a single column: 12 first rows of the column "Invoice"
print("12 first rows of the column 'Invoice' ")
print(auto['Invoice'].head(12))
print()
# or 
print(auto.Invoice.head(12))
print()

# select multiple columns:
list_columns = ['Invoice' , 'Make','Body_Style' , 'Price']
print('select multipel columns from <auto> data frame')
auto_part = auto[ ['Invoice' , 'Make','Body_Style' , 'Price'] ]
print(auto_part)

# filter <auto> data frame by rows position and column names
print()
print('select rows with indexes from 22 to 44 and the columns <Invoice>, <Make>, <Price>')
print(auto.loc[auto.index[22:44] , ['Invoice','Make','Price']])
print()
print()
print('select last 33 rows and the columns <Make> , <Body_Style> , <City_mpg> , <Highway_mpg>, ')
print(auto.loc[auto.index[-33:] , ['Make' , 'Body_Style' , 'City_mpg' , 'Highway_mpg']])

# --------------------------------------------------------------------------------------------------------

# filter <auto> data frame by row position and column position
print("select rows and columns by their position")
print('first 7 rows')
print(auto.iloc[:7])
print('last 8 rows')
print(auto.iloc[-8:])
print("rows from 30 to 45")
print(auto.iloc[30:46])
print()
print('last 4 columns')
print(auto.iloc[ : , -4:])
print('first 20 rows, first 5 columns')
print(auto.iloc[ :20 , : 5])
print()
print('rows from 55 to 105 by their position , columns from 2 to 8')
print(auto.iloc[55:105 , 2:8])
print()
print('last 20 rows and the columns from 5 to 10')
print(auto.iloc[-20: , 5:10])
print()

print('filter dataframe using a list of values')
print('<auto> datarame: imported cars with normalized loss 0 and 150')
print(auto[auto['Normalized_Loss'].isin([ 150,0])])
print()
print('<auto> dataframe: imported cars with make saab, peugot, mazda')
print(auto[auto['Make'].isin(['saab','peugot','mazda'])])
print()

# select multiple columns
print('select multiple columns of <auto> dataframe')
print( auto[ ['Invoice','Make','Body_Style','Price'] ] )

# -----------------------------------------------------------------------------------

'''
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


# filter out the column "Normalized_Loss" to get rid of '0' values
auto_loss = auto.loc[auto["Normalized_Loss"] > 0 ]
print()
print()
print(auto_loss)
# sort <auto> data frame by the column <Normalized_Loss>
auto_loss_asc = auto_loss.sort_values( by = ['Normalized_Loss'] ,
                                        ascending = True ,
                                        inplace = False )

print()
print()
print(' <auto_sort_loss_asc>  data frame : ')
print(auto_loss_asc)
'''