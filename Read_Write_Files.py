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