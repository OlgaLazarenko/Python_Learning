# Read_Write_Files
#!/bin/python3


import pandas as pd
import os

# read the data from the file <Auto_Import_1985.csv"
auto = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv")
# print the first 5 rows
print(auto.head())
print()
print(' ---  Columns of <auto> data frame   ---')
for rows in auto.columns:
    print(rows)
print()

# rename columns of <auto> data frame
auto.rename( columns = { 'Normalized Loss' : 'Normalized_Loss',
                        'Fuel Type' : 'Fuel_Type' ,
                        'Num of Doors' : 'Num_of_Doors' ,
                        'Body Style' : 'Body_Style' ,
                        'Drive Wheels' : 'Drive_Wheels' ,
                        'Engine Location' : 'Engine_Location' ,
                        'Wheel Base' : 'Wheel_Base' ,
                        'Engine Type' : 'Engine_Type' , 
                        'Num of Cylinders' : 'Num_of_Cylinders' , 
                        'Engine Size' : 'Engine_Size' ,
                        'Fuel System' : 'Fuel_System' ,
                        'Compression Ratio' : 'Compression_Ratio' ,
                        'Peak rmp' : 'Peak_rmp' ,
                        'City mpg' : 'City_mpg' ,
                        'Highway mpg' : 'Highway_mpg'

                        } , inplace = True
            )
print()
print()
print(' ---  New column names of <auto> data frame   ---')
for col in auto:
    print(col)
# --------------------------------------------------------------------------------------------------
# write the data to files according to the car make
# df.to_csv('file_name.csv')
auto.to_csv("file_name")

auto_make_list = auto.Make.unique() # list containing the unique car make
for make in auto_make_list :
    file_name_part1 = "E:\\_Python_Projects_Data\\Auto_Files\\"
    file_name_part2 = make
    file_name_part3 = ".csv"
    file_name = file_name_part1 + file_name_part2 + file_name_part3

    # check if the file exists
    
# avoid index column to be written to new csv. file

auto.to_csv(file_name)  # write .csv files 

  
# unique values of the column <Make>
print()
print(' -- unique values of the column <Make>')
for car_make in auto_make_list:
    print(car_make)

# write the data frame <auto> to a new csv file
auto.to_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Car_Import_1985.csv" , index = False)

# check of the file "Car_Import_1985.csv" exists
print()
if os.path.isfile("E:/_Python_Projects_Data/Data_Visualization/Autos_Data_Set/Car_Import_1985.csv") :
    print("File  'Car_Import_1985.csv'  exists")
else:
    print("File  'Car_Import_1985.csv' does not exist")

print()
print()
# read the data from the file <Auto_Import_1985.csv"
auto = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Car_Import_1985.csv")
# print the first 5 rows
print(auto.head())
print()
print(auto.dtypes)

