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

# create a dataframe <college_df_default_and_my_index>

college_df_my_index.reset_index(inplace = True)
print()
print()
print('<college_df_default_and_my_index>')
print(college_df_my_index)
print()
print()


# create my own index column and remove the default index column
my_index_col = { 'AAA' , 'BBB' , 'CCC' , 'DDD' , 'EEE'}

# convert the dictionary <college_class> and <my_index_col> into a dataframe
college_df_my_index_col = pd.DataFrame(college_class, my_index_col)
college_df_my_index_col_2 = pd.DataFrame(college_class, my_index_col)
print(' <college_df_my_index_col>  DataFrame')
print(college_df_my_index_col)
print()
print()

# reset/remove my own index and make the default index as index
# use <college_df_my_index_col>
print("Resent/remove my own index and make the default index as index")
print(' from <college_df_my_index_col')
# remove my own index 
college_df_my_index_col.reset_index(inplace = True , drop = True)
print(college_df_my_index_col)
print()
print()


# make the column <Last_Name> as the index column, remove the default index column
index_column = {'a','b','c','d','e'}
college2 = pd.DataFrame(college_class , index_column)
print("<college_df_2>")
college2.set_index(['Last_Name'] , inplace = True)
print(college2)
print()
# make the column <First_Name" as the index column
college2.set_index(['First_Name'] , inplace = True)
print('---------------------------')
print()
print(college2)