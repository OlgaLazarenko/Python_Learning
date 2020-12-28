#!/bin/python3

import pandas as pd

# cread a DataFrame using a list of lists
honda_cars = {'Honda Model':['Civic','Accord','Acura','Pilot','Odyssey','Fit','Ringline', 'Civic','HR-V','Civic'] ,
                 'Year':['2005','2012','2018','2020','2013','2019','2020','2019', '2014','2000'] , 
                 'Mileage':[98600,55000,16000,126000,150000,17000,500,10000,110000,95000] ,
                 'Price': [6500,12300,15500,18000,77000,16600,34000,19000,12000,5000] ,
                 'Category': ['sedan','sedan','sedan','suv','minivan','hatchback','truck', 'sedan','suv','sedan']
                 
                 }
# create the dataframe 'df_honda_cars'
df_honda_cars = pd.DataFrame(honda_cars)


print('dataframe "honda_cars"')
print(df_honda_cars)
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
