#!/bin/python3

import pandas as pd

# cread a DataFrame using a list of lists
honda_cars = {'Honda Model':['Civic','Accord','Acura','Pilot','Odyssey','Fit','Ringline', 'Civic Hatchback','HR-V','Civic'] ,
                 'Year':['2005','2012','2018','2020','2013','2019','2020','2019', '2014','2000'] , 
                 'Mileage':[98600,55000,16000,126000,150000,17000,500,10000,110000,95000] ,
                 'Price': [6500,12300,15500,18000,77000,16600,34000,19000,12000,5000] ,
                 'Category': ['sedan','sedan','sedan','suv','minivan','hatchback','truck', 'hatchback','suv','sedan']
                 
                 }
# create the dataframe 'df_honda_cars'
df_honda_cars = pd.DataFrame(honda_cars)


print('dataframe "honda_cars"')
print(df_honda_cars)