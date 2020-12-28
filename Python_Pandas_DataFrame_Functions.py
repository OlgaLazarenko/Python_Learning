#!/bin/python3

import pandas as pd

# cread a DataFrame using a list of lists
honda_cars = {'Honda Model':['Civic','Accord','Acura','Pilot','Odyssey','Fit','Ringline', 'Civic','HR-V','Civic', 'Accord'] ,
                 'Year':['2005','2012','2018','2020','2013','2019','2020','2019', '2014','2000','2001'] , 
                 'Mileage':[98600,55000,16000,126000,150000,17000,55000,10000,110000,95000,100000] ,
                 'Price': [6500,12300,15500,18000,17000,16600,34000,19000,12000,5000,6500] ,
                 'Category': ['sedan','sedan','sedan','suv','minivan','hatchback','truck', 'sedan','suv','sedan','sedan'],
                 'Condition': ['good','fair','good','excellent','good','fair','excellent','fair','bad','good','bad']
                 
                 }

print()
print()
# create the dataframe 'df_honda_cars'
df_honda_cars = pd.DataFrame(honda_cars)


print('dataframe "honda_cars"')
print(df_honda_cars)
print()


#   ***   pandas.DataFrame.sort_values    ***
# ---  dataframe.sort_values(by, axis,ascending,inplace,kind,na_position,ignore_index, key)  ---

# inplace = False is the default option, if not mentioned

print('1)  sort by the price(desc) without updating the initial dataframe(inplace parameter is not mentioned, by the default = False)')
print(df_honda_cars.sort_values(by = 'Price' , ascending = False))
print('-*-*-*-') 
print()
print('2) sort by the model/asc, year/desc, mileage/desc without the updating the dataframe')
print(df_honda_cars.sort_values( by = ['Honda Model','Year','Mileage'] , ascending = [True, False, False]))
print()


# sort the dataframe with inplace = True, the initial dataframe will be upadated
df_honda_cars.sort_values( by = 'Honda Model' , inplace = True)
print('sorted and updated dataframe')
print(df_honda_cars)
print()

# sort the dataframe with inplce = False, the default option; 
# in this case only a sorted copy is returned, the dataframe stayed without changes
print('the copy of the dataframe, sorted by year column')
print(df_honda_cars.sort_values( by = 'Year'))
print()
print('*--------*')
print("the dataframe df_honda_cars")
print(df_honda_cars)
print()
print('sort with inplace = False and assign this copy to a new variable df_honda_cars_sorted_mileage')
df_honda_cars_sorted_copy = df_honda_cars.sort_values( by = 'Mileage')
print(df_honda_cars_sorted_copy)

# thus now we have two dataframes: 
# the updated df_honda_cars arranged by "Honda Model" column in ascending way
# and the dataframe df_honda_cars_sorted_mileage the result of sorting by "Mileage" column and assigning to the new dataframe

