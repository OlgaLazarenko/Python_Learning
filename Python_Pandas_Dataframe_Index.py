# Dataframe index
#!/bin/python3


import pandas as pd
import numpy as np
import random

# create a dataframe from a dictionary
# dictionary
college_class = {
                'Last_Name': ['Stephenson' , 'Pizaro' , 'Kim' , 'Williams' , 'Hua'] ,
                'First_Name': ['Grace', 'Maria', 'Lola', 'John' , 'Sofia'] ,
                'Age' : [22,30,27,19,45, 40] ,
                'Grade' : ['B','C','A','A','D']
               }
print()
print('dictionary:')
print(college_class)
# list to create the index column
print()
print('list to create the index column')
