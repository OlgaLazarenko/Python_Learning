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
                'Age' : [22,30,27,19,45] ,
                'Grade' : ['B-','C','A','A+','D']
               }


# create a dataframe <college_df> with the default index column
college_df = pd.DataFrame(college_class)
print()
print(' <college_df> dataframe')
print(college_df)
print()

# create a dataframe <college_df_my_index> with my own index column
print()
print('dictionary:')
print(college_class)
# dictionary  to create the index column
print()
print('list to create the index column')
list_index = { '001', '002' , '003' ,'004','005'}
print(list_index)
print()

college_df_my_index = pd.DataFrame(college_class, list_index)
print(' <college_df_my_index>  dataframe')
print(college_df_my_index)

