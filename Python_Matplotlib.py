#!/bin/python3

#    ***   Loading data from files for Matplotlib   ***
# extract data from a .csv file and graph it

import matplotlib.pyplot as plt
import csv # use this module to load .csv file
'''
x = [] # declare the list for x-axis
y = [] # declare the list for y-axis

with open('E:\_Python_Projects_Data\Public_Assistance_Programs_US\SNAP_History.csv','r') as data_file :
    my_plots = csv.reader(data_file, delimiter = ',')
    data_file.readline() # to skip the columns name and not add to the lists
    for row in my_plots :
        x.append(int(row[0])) # populate the list with the values of the first column "Fiscal Year" of the data file
        y.append(int(row[1])) # populate the list with the values of the second column "Average Participation" of the data file
        
        

    print(x)
    print()
    print(y)

print()
print()

plt.plot(x,y, label = 'SNAP Program, 1969-2019')
plt.xlabel('fiscal year')
plt.ylabel('average participation')
plt.title('Public Assistance, US')
plt.legend()
# plt.show()
print()
print()
'''
# ------------------------------------------------------------------------
# plot the data from the file Patents.csv
# load the data from the file
import pandas as pd
patent_data = pd.read_csv("E:\_Python_Projects_Data\Patents\Patents.csv")
print('type: ')
print(type(patent_data))
print()
print(patent_data.head()) # display the first 5 rows 
print()
# retrieve the data to create a plot year/patents_applied for public and private sector

# patents at private sector
private_patents_data = patent_data[patent_data.sector == "Private Sector"]
print("Patents at Private Sector")
print(private_patents_data)
print()
x = private_patents_data.year
y = private_patents_data.patents_applied

plt.plot(x,y)

# patents at public sector
public_patents_data = patent_data[patent_data.sector == "Public Sector"]
print("Patents at Public Sector")
print(public_patents_data)
z = public_patents_data.patents_applied
plt.plot(x,z)
plt.legend(["Private Sector", "Public Sector"])
plt.show()



# x-axis will be the column 'year'
# at y-axis will show the number of patents applied 
# display the number of applied patents over time for the private and public sector

