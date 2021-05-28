# Read_Write_Files
#!/bin/python3


import pandas as pd

# read the data from the file <Auto_Import_1985.csv"
auto = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv")
# print the first 5 rows
print(auto.head())
print()


# unique values of the column <Make>
print('unique values of the column <Make>')
auto_make_list = auto.Make.unique()
print(auto_make_list)

# write the data to a file
# df.to_csv('file_name.csv')
auto.to_csv("file_name")


for make in auto_make_list :
    file_name_part1 = "E:\\_Python_Projects_Data\\Auto_Files\\"
    file_name_part2 = make
    file_name_part3 = ".csv"
    file_name = file_name_part1 + file_name_part2 + file_name_part3
    auto.to_csv(file_name)
   

