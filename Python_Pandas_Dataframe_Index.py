# Dataframe index
#!/bin/python3


import pandas as pd
import numpy as np
import random

# create a dataframe from a dictionary
# dictionary
college_dict = {
                'Last_Name': ['Stephenson' , 'Pizaro' , 'Kim' , 'Williams' , 'Hua'] ,
                'First_Name': ['Grace', 'Maria', 'Lola', 'John' , 'Sofia'] ,
                'Age' : [22,30,27,19,45] ,
                'Grade' : ['B-','C','A','A+','D'] , 
                'Graduate_Year' :[ '2021','2022','2000','2021','2021']
               }

# the initial dictionary to be used for a DataFrame <college_df>
print()
print("The initial dictionary to be turned into a DataFrame <college_df> :")
print('=====================================================')

# create a DataFrame <college_df> with the default index column
college_df = pd.DataFrame(college_dict)
print()
print(' <college_df> DataFrame with the default index column:')
print(college_df)
print()
print('*---------------------------------------------------*')
print('**  DataFrame  <college_df>  information:')
print('--> size:')
df_size = college_df.size
print(df_size)
print()
print('--> shape')
df_shape = college_df.shape
print(df_shape)
print()
print('--> information')
df_info = college_df.info
print(df_info)
print()
print('values data types ')
print(college_df.dtypes)
print('--------------------')


print(" <college_df_my_index> DataFrame with my own index column")
# dictionary  to create the index column
my_index = { 'Student1', 'Student2' , 'Student3' ,'Student4','Student5'}
college_df_my_index = pd.DataFrame(college_df, my_index)
print()
print(college_df_my_index)
print()
print()


print("<college_df_default_index_and_my_index> DataFrame")
print("  with the default and my own index column")
college_df_my_index.reset_index(inplace = True)
print()
print()
print('<college_df_default_and_my_index>')
print(college_df_my_index)
print()
print()
print('Set MultiInxed for the DataFrame <college_dg>')
print(college_df)
college_df_multi_index = college_df.set_index(['Grade','Graduate_Year'])
print(college_df_multi_index)
print()

# loc() wtih multiple conditions
print('<college_df> with the column <Age> ') # column "Age" is intt4 data types
print(college_df.loc('Age'))
print()
print('*******************************************')



'''
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
print(' initial <college2> dataframe ')
college2 = pd.DataFrame(college_class , index_column)
print('*-------------------------------------------*')
print(college2)
print('*-------------------------------------------*')
print()
print()
# make the column <Last_Name" as the index column
print('<Last_Name> column substituted the index column')
college2.set_index(['Last_Name'] , inplace = True)
print(college2)
print()
print()
# insert a new index column again, use index_column dictionary



# make the column <First_Name" as the index column
college2.set_index(['First_Name'] , inplace = True)
print('----------------------------------------------')
print()
print('<First_Name> column substituted the index column <Last_Name>')
print(college2)
print()
print('------------------------------------------------')


# 1) Indexing Operator []
print(" *** Indexing Operator [] ")
print()
print('select a single column <Last_Name>')
print(college_class['Last_Name'])
print()
print('select a single column <First_Name>')
print(college_class['First_Name'])
print()
print('select a single column <Grade>')
print(college_class['Grade'])
print('      -------------------------------------------')
print()



print(' select multiple columns')

df_1 = college_class[ ["First_Name","Last_Name"] ]
print(df_1)
'''