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
                'Student_ID': [10011,10022,10033,10044,10055] ,
                'Last_Name': ['Stephenson' , 'Pizaro' , 'Kim' , 'Williams' , 'Hua'] ,
                'First_Name': ['Grace', 'Maria', 'Lola', 'John' , 'Sofia'] ,
                'Age' : [22,30,27,19,45] ,
                'Grade' : ['B-','C','A','A+','D'] , 
                'Graduate_Year' :[ '2021','2022','2000','2021','2021'] , 
                'Major' : ['Biology','Math','Art','Math','History']
               }

# the initial dictionary to be used for a DataFrame <college_df>
print()
print("The initial dictionary to be turned into a DataFrame <college_df> :")
print('=====================================================')

# create a DataFrame <college_df> with the default index column
college_df = pd.DataFrame(college_dict)
# student_df = pd.DataFrame(college_dict, index_col = ['Student_ID'])
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

print("             * column 'Grade'")
print(College_DF['Grade'] , "\n")

print("             * column 'Grade ")
print(College_DF['Grade'], "\n")

print("              * columns 'LastName', 'Age' ")
print(College_DF[['LastName','Age']] , "\n")

print("               * columns 'LastName', 'Grade', 'GraduateYear' ")
print(College_DF[['LastName','Grade','GraduateYear']] , "\n")

print("          * select all rows and some columns ('LastName', 'FirstName','Age')")
print(College_DF[['FirstName','LastName','Age']], "\n")


print('********************************************************************')
print('3) LOC() METHOD')
print("      loc() methond and <College_DF>  data frame")
print("             index 'Student_02")
print(College_DF.loc['Student_02'] ,"\n" )

print("             * index 'Student_04'")
print(College_DF.loc['Student_04'] ,"\n")




print('!!! Notice changes: ')
print("            * row index 'Student_01','Student_03','Student_05'" ,"\n")
print(College_DF.loc[['Student_01','Student_03','Student_05']] , "\n")


print("           * the range for the row index from 'Student_01' to 'Student_04'")
print(College_DF.loc['Student_01':'Student_04'], "\n")

print("          * select all rows and the column 'LastName'")
print(college_df.loc[ :,'Last_Name'], "\n")

print("           * select with a list of labels, rows and columns, College_DF")
print(College_DF.loc[ ['Student_01','Student_02'] , ['FirstName','Age']] , "\n" )

print("           * select with a list of labels, rows and columns, college-df")
print(college_df.loc[ [1,2,3] , ['Last_Name','Age','Grade'] ] , "\n")

print("            * retrieve with a slice of rows and columns, college_df")
print(college_df.loc[1:3 ,'First_Name' : 'Grade'] , "\n" )
print(college_df.loc[1:3 , 'First_Name':'Graduate_Year'] , "\n")
print(college_df.loc[2:5 , 'Age':'Graduate_Year'] , "\n")

print("            * retrieve with a slice of rows and columns, College_DF")
print(College_DF.loc[ 'Student_01':'Student_04' , 'FirstName':'Age'] , "\n")
print(College_DF.loc[ 'Student_02':'Student_05' , 'LastName':'GraduateYear'] , "\n")
print(College_DF.loc[ 'Student_03':'Student_05' , 'Age':'Grade'] , "\n")

print("            * retrieve the data with a list of values/rows,colulmns, College_DF dataframe")
print(College_DF.loc[ ['Student_01','Student_03','Student_05' ]] , "\n" )
print(College_DF.loc[ : , ['LastName','FirstName']] , "\n")
print(College_DF.loc[ ['Student_01','Student_02'] , :] , "\n")
print('>>> College_DF  dataframe')
print(College_DF.loc[:,:] , "\n")
print('>>> college_df  dataframe')
print(college_df.loc[:,:] , "\n")
print()

print("************************************************************************")
print("  6) Retrieve data using list of labels :", "\n")
list_rows_1 = ['Student_01','Student_02','Student_03']
list_rows_2 = ['Student_04','Student_05']
list_rows_3 = ['Student_01','Student_03','Student_05']

list_columns_1 = ['LastName','Age']
list_columns_2 = ['FirstName','LastName','Age','Grage']
list_columns_3 = ['LastName','FirstName','Major']

print("  >>>  with loc() method:")
print(College_DF.loc[list_rows_1 , list_columns_1] , "\n")
print(College_DF.loc[list_rows_2 , list_columns_2] , "\n")
print(College_DF.loc[ ['Student_01','Student_02'] , : ] , "\n")
print(College_DF.loc[:, list_columns_1] , "\n")
print(College_DF.loc[ ['Student_01','Student_04'] , :] , "\n")
print(College_DF.loc[ ['Student_01','Student_02'] , ['FirstName','LastName'] ] , "\n")
print(College_DF.loc[ ['Student_01','Student_05'] , ['LastName','Age']] , "\n")

# print(College_DF.loc[ ['Student_01','Student_03','Student_05'] ,
#                        ['FirstName','Age','Major'] ] ) ??? Why an error???




'''
print(College_DF.loc[list_rows_2 , list_columns_2] , "\n" )
print(College_DF.loc[list_rows_3 , list_columns_3], "\n")


print("  >>>  with iloc() methond")




print(" 4) Selection via conditions ")
print('select students with Student_ID > 10022 from college_df DataFrame')
print(college_df.loc['Student_ID' > 10022])
print()

print(" >>> student_df  DataFrame : ")
print(student_df , "\n" )

print("retrive a single value with iloc() function from student_df DataFrame")
print("with Student_ID = 10044 ")
print(student_df.iloc['10044'])


print("**************************************************************************")
print()
print(" 4) iloc() method") # retrieve values belonging to a row/column with a specific index
# iloc() function accepts only integer types values as index values
print('>>> the initial dataframe "College_DF"')
print(College_DF, "\n") 
# the columns: FirstName, LastName, Age, Grade, GraduateYear
# 5 rows, the index from 0 to 4
print('select from 2nd (index 3) to 4th (index 5) rows')
print(College_DF.iloc[1:4] , "\n")
print('select from 1st/index=0 to 2nd/index=1 rows')
# n-1, n is the row number/location
# start row, finish row
start = 1
finish = 2
print(College_DF.iloc[:2], "\n")
print(College_DF.iloc[start-1:finish] , "\n")

print(" >>> the first row of College_DF")
print(College_DF.iloc[0] , "\n")

print(" >>> the second row of College_DF")
print(College_DF.iloc[2] , "\n")

print(" >>> the first column of College_DF")
print(College_DF.iloc[: , 0] , "\n")

print(" >>> the second column of College_DF")
print(College_DF.iloc[: , 1] , "\n")

print(" >>> the first and second column of College_DF")
print(College_DF.iloc[:, 0:2] , "\n")

print(" >>> from the  second to  fourth column of College_DF")
print(College_DF.iloc[:, 2:5] , "\n")

print(" >>> from the  second to  fourth column of College_DF")
print(College_DF.iloc[:, 2:5] , "\n")

print(" >>> from the second to third rows and from the first to second column of College_DF")
print(College_DF.iloc[ 1:3, 0:2] , "\n")

print(" >>> from the first to fourth rows and from the second to the last column of College_DF")
print(College_DF.iloc[ :4, 1:] , "\n")







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