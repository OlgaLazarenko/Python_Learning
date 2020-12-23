#!/bin/python3
# Loading data from files for Matplotlib
# extract data from a .csv file and graph it

import matplotlib.pyplot as plot
import csv # use this module to load .csv file

x = [] # declare the list for x-axis
y = [] # declare the list for y-axis

with open('E:\_Python_Projects_Data\Public_Assistance_Programs_US\SNAP_History.csv','r') as data_file :
    my_plots = csv.reader(data_file, delimiter = ',')
    for row in my_plots :
        x.append(int(row[0])) # populate the list with the values of the first column "Fiscal Year" of the data file
        y.append(int(row[1])) # populate the list with the values of the second column "Average Participation" of the data file



