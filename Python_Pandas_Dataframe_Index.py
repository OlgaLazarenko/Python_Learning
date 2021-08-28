# Dataframe index
#!/bin/python3


import pandas as pd
import numpy as np
import random
print("\n"*3)
print(' *-*  PROJECT:  INDEXING  *-* ', "\n")
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
print(college_df ,"\n" )
print()
print('*---------------------------------------------------*')

print('**  DataFrame  <college_df>  information:')

print('--> Size:')
df_size = college_df.size
print(df_size, "\n")

print('--> Shape')
df_shape = college_df.shape
print(df_shape , "\n")

print('--> Information')
df_info = college_df.info
print(df_info , "\n")

print('Values Data Types ')
print(college_df.dtypes)
print('--------------------')


print(" <college_df_my_index> DataFrame with my own index column")
# dictionary  to create the index column
my_index = { 'Student1', 'Student2' , 'Student3' ,'Student4','Student5'}
college_df_my_index = pd.DataFrame(college_dict, my_index )
print(college_df_my_index , "\n")
college_df_my_index2 = college_df_my_index


print("<college_df_default_index_and_my_index> DataFrame")
print("  with the default and my own index column")
college_df_my_index2.reset_index(inplace = True)
print('***************************************************************')
print(college_df_my_index , "\n")

print('<college_df_default_and_my_index>')
print(college_df_my_index ,("\n"*2))
print()
print()
print('Set MultiInxed for the DataFrame <college_dg>')
print('** The initial DataFrame:')
print(college_df)

college_df_multi_index = college_df.set_index(['Grade','Graduate_Year'])
print(college_df_multi_index ,"\n" )

print('-----*-----*-----')
print()

# loc() method
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(" I) <college_df>  DataFrame")
print(college_df)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')



College_DF = pd.DataFrame(           
            [     
                ['Thomas' , 'Johnson', '22' , 'A' , '2020'] ,
                ['Grace', 'Martinez', '25', 'B' , '2021'] ,
                ['Maria', 'Smith', '36', 'F', '2028'] ,
                ['Olga', 'Lazarenko', '29', 'A', '2000'] , 
                ['Alex', 'ONeil', '18', 'D','2023'] 
                
            ] ,
            index = ['Student_01' , 'Student_02', 'Student_03', 'Student_04','Student_05'] , 
            columns =['FirstName' , 'LastName','Age','Grade','GraduateYear']
)   
print(" II) <College_DF>  DataFrame:")
print(College_DF)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

print()
print('1) INDEXING OPERATOR/[]' , "\n")

print("            * retrieve all rows and the column 'LastName'")
print(College_DF["LastName"], "\n")


print('********************************************************************')
print('2) LOC() METHOD')
print("      loc() methond and <College_DF>  data frame")
print("             index 'Student_02")
print(College_DF.loc['Student_02'] ,"\n" )

print("             * ndex 'Student_04'")
print(College_DF.loc['Student_04'] ,"\n")

print('!!! Notice changes: ')
print("            * row index 'Student_01','Student_03','Student_05'" ,"\n")

print(College_DF.loc[['Student_01','Student_03','Student_05']])
print("             index'Grade'" ,"\n")

print("           * the range for the row index from 'Student_01' to 'Student_04'")
print(College_DF.loc['Student_01':'Student_04'],"\n" )

print("          * select all rows and the column 'LastName'")
print(college_df.loc[ :,'Last_Name'], ("\n"*2))

print("          * select all rows and some columns ('LastName', 'FirstName','Age')")
print(College_DF.loc[:, ['FirstName','LastName','Age']])



'''
print(college_df_my_index.loc['First_Name'])
print()
print()
print(college_df.loc[:,:])
print()
print(college_df.loc[2:,:])
print()
print(college_df.loc[4:5 , :])
print('*******************************************')




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