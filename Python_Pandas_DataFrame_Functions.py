#!/bin/python3

import pandas as pd
import numpy as np

# cread a DataFrame using a list of lists
honda_cars = {'Honda Model':['Civic','Accord','Acura','Pilot','Odyssey','Fit','Ringline', 'Civic','HR-V','Civic',np.nan, 'Accord', np.nan] ,
                 'Year':['2005','2012','2018','2020','2013','2019','2020','2019', '2014','2000','2002','2001','2005'] , 
                 'Mileage':[98600,55000,16000,126000,150000,17000,55000,10000,110000,95000,66000,100000, 75000] ,
                 'Price': [6500,12300,15500,18000,17000,16600,34000,19000,12000,5000,2200,6500,11000] ,
                 'Category': ['sedan','sedan','sedan','suv','minivan','hatchback','truck', 'sedan','suv','sedan','sub','sedan', 'van'],
                 'Condition': ['good','fair','good','excellent','good','fair','excellent','fair','bad','good','good','bad','good']
                 
                 }

print()
print()
# create the dataframe 'df_honda_cars'
df_honda_cars = pd.DataFrame(honda_cars)


print('dataframe "honda_cars"')
print(df_honda_cars)
print()


#   ***   pandas.DataFrame.sort_values    ***
# ---  dataframe.sort_values(by,axis,ascending,inplace,kind,na_position,ignore_index, key)  ---
# --- by the default axis = 0, ascending = True, inplace = False, na_position = 'last' , kind = 'quicksort', ignore_index=False, key = None
# inplace = False is the default option, if not mentioned

# sort_values, with the parameter 'by = ['...','...']
print('1)  sort by the price(desc) without updating the initial dataframe(inplace parameter is not mentioned, by the default = False)')
print(df_honda_cars.sort_values(by = 'Price' , ascending = False))
print('-*-*-*-')
print()
print()


print('2) sort by the model/asc, year/desc, mileage/desc without the updating the dataframe')
print(df_honda_cars.sort_values( by = ['Honda Model','Year','Mileage'] , ascending = [True, False, False]))
print('-*-*-*-')
print('the NaN values at the model column now located at the bottom of the column') 
print()
print()

# sort the dataframe with inplace = True, the initial dataframe will be upadated
print('3) sort the dataframe by the model, the parameter inplace=True and update dataframe')
print(df_honda_cars.sort_values( by = 'Honda Model' , inplace = True)) # nothing will be returned
print('---')
print('the updated dataframe with models sorted asc')
print(df_honda_cars)
print()

# sort the dataframe with inplce = False, the default option; 
# in this case only a sorted copy is returned, the dataframe stayed without changes
print('4) sort the dataframe with the paramert input = False, create a copy of the dataframe, sorted by year column')
print(df_honda_cars.sort_values( by = 'Year'))  
print()
print('*--------*')
print("the dataframe df_honda_cars")
print(df_honda_cars)
print()
print('5) sort with inplace = False , Mileage desc ,assign the copy to a new variable df_honda_cars_sort_mileage')
df_honda_cars_sort_mileage = df_honda_cars.sort_values( by = 'Mileage')
print()
print('new dataframe  df_honda_cars_sort_mileage')
print(df_honda_cars_sort_mileage)
print('-*-*-*-')
print()
print()

# thus now we have two dataframes: 
# the updated df_honda_cars arranged by "Honda Model" column in ascending way
# and the dataframe df_honda_cars_sorted_mileage the result of sorting by "Mileage" column and assigning to the new dataframe

# put NaN values last
print('6) NaN values are last')
print(df_honda_cars.sort_values( by = "Honda Model"))
print('-*-*-*-')
print()
print()

# put NaN values first
print('6) putting NaN values first')
print(df_honda_cars.sort_values( by = "Honda Model" , na_position = 'first') )
print('-*-*-*-')
print()
print()

# ----------------------------------------------------------------------------------------
my_df = pd.DataFrame( [ [ 5,3,7,2,-1], [0,-6,10,1,8], [10,25,18,30,73] ] , 
                     index = ['row1','row2','row3'] ,
                     columns = ['col1', 'col2', 'col3', 'col4', 'col5']
                  )
print("New data frame  'my_df' : ")
print()
print(my_df)
# get a value from the column 'col2' and the row 'row3'
print("get a value from the column 'col2' and the row 'row3'")
value_row3_col2 = my_df.at['row3', 'col2']
print("value_col2_row3: " + str(value_row3_col2))

value_row1_col1 = my_df.at['row1', 'col1']
print("value_row1_col1: " + str(value_row1_col1))

value_row2_col2 = my_df.at['row2','col2']
print('value_row2_col2: ' + str(value_row2_col2))

value_row3_col5 = my_df.at['row3','col5']
print('value_row3_col5: ' + str(value_row3_col5))

# we can change elements at the data frame, set them for a new values
# df.at[row,col] = new_value
print()
print('Change elements at the data frame, set them for a new values')
my_df.at['row1', 'col1'] = 500
my_df.at['row2','col5'] = 100
my_df.at['row3','col4'] = 0

print(my_df)
print()

# the max value of a column
max_col1 = my_df['col1'].max()
print('max_col1: ' +  str(max_col1))

# the index of the max value of a column
index_max_col1 = my_df['col1'].idxmax()
print('the index of max_col1: ' + str(index_max_col1))

# ------------------------------------------------------

max_col2 = my_df['col2'].max()
print('max_col2 : ' + str(max_col2))

index_max_col2 = my_df['col2'].idxmax()
print('the index of max_col2 : ' + str(index_max_col2))
print()

# the min value of a column
min_col4 = my_df['col4'].min()
print('min_col4 : ' + str(min_col4))


# the index of the min value of a column
index_min_col4 = my_df['col4'].idxmin()
print('the index of min_col4 : ' + str(index_min_col4) )
print('-----------------------------------')

# the max value of the data frame
max_df_rows = my_df.max(axis = 0) # index (0)
max_df_cols = my_df.max(axis = 1) # columns(1)
print()
print(my_df)
print()
print("max_rows/axis=0")
print(max_df_rows)
print()
print("max_cols/axis=1 ")
print(max_df_cols)
print('-------------------------------------')
print()
# select rows by multiple label/index conditions
print('select rows by multiple label conditions')
print()
print('Data Frame')
print(my_df)
print()
print("select the values of the data frame if the values in the column 'col2' > 0")
my_df1 = my_df.loc[my_df['col2'] > 0]
print(my_df1)
print()
print("select the values of the data frame if the values in the column 'col3' >= 10")
my_df2 = my_df.loc[my_df['col3'] >= 10]
print(my_df2)
print()
print("select the values of the data frame with multiple rows conditions")
print('col2 > 0  and col5 > 0')
my_df3 = my_df.loc[ (my_df['col2'] > 0) & (my_df['col5']> 0)]
print(my_df3)
print()
print(my_df)
print()
print("select the values of the data frame with multiple rows conditions")
print('col1 >= 10 and col2 > 0')
my_df4 = my_df.loc[ (my_df['col1'] >= 10) & (my_df['col2'] >= 0)]
print(my_df4)
print()

print(my_df)
print()
print("select the values of the data frame with multiple rows conditions")
print('col3 > 7 or col5 > 0')
my_df5 = my_df.loc[ (my_df['col3'] > 7) | (my_df['col5'] > 0)]
print(my_df5)
print()
print("select the values of the data frame with multiple rows conditions")
print('( col1 > 0  and col2 > 0 ) or (col3 > 7 and col5 = 100)')
my_df6 = my_df.loc[((my_df['col1']>0) & (my_df['col2']>0)) | ((my_df['col3']>7) & (my_df['col5']== 100))]
print(my_df6)