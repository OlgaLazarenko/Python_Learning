#!/bin/python3

#    ***    Working with Numpy    *** 

#  Loading data from .csv file using Numpy module

import matplotlib.pyplot as plt
import numpy as np

x , y = np.loadtxt('E:\_Python_Projects_Data\Data_Sales.csv' ,
                    delimiter = ',' , unpack = True)
plt.plot(x , y , label = "Sales History")

plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Information')
plt.legend()
plt.show()