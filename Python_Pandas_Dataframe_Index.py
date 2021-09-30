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
                'Grade' : ['B-','C','A','A','B'] , 
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
# print(College_DF.loc[list_rows_2 , list_columns_2] , "\n")

print("***********************************************************************", "\n")

print(' >>> 4) Selection via Condition/ ' , "\n")
        # a) loc() with conditions (single, multiple)
        # b) iloc() with conditions (single, mulitple)
print('..... 4(a) loc() with conditions (single, multiple)')
print('- students with major "Math"')
print(college_df.loc[college_df.Major == 'Math',:], "\n")

print('select student with age = 22')
print(college_df.loc[college_df.Age == 22] , "\n" )
print(college_df.loc[college_df.Age == 22 , : ] , "\n") # the output is the same with the previous line of code

print('- students with grade = A')
print( college_df.loc[college_df.Grade == 'A' , : ] , "\n" )

print('- students with graduate year = 2021')
print( college_df.loc[college_df.Graduate_Year == '2021'] , "\n")

print('- students with age>25')
print(college_df.loc[college_df.Age > 25] , "\n")

print('- students with grade A and graduate year > 2000')
print(college_df.loc[ (college_df.Grade == 'A') 
                        & (college_df.Graduate_Year > '2000')
                    ], "\n")

print("- students with the major = 'Math' and grade C")
print(college_df.loc[ (college_df.Major == 'Math') 
                        & (college_df.Grade == 'C')
                    ] , "\n")

print("- students first name, age, major with the age > 20, the grade = A and graduate year 2021")
print(college_df.loc[ (college_df.Age > 20) 
                            & (college_df.Grade == 'A') 
                                & (college_df.Graduate_Year == '2000')
                    ] , "\n'")

print('- students first and lasta name with age>25')
print(college_df.loc[ (college_df.Age > 25) , 
                        ['Last_Name','First_Name']
                    ] , "\n")

print('- students with grade A and graduate year > 2000')
print(college_df.loc[ (college_df.Grade == 'A') 
                        & (college_df.Graduate_Year > '2000') , 
                        ['Last_Name','Grade','Graduate_Year']
                    ], "\n")

print("- students with Student_Id, first name, age, major, graduate year with the age > 20, the grade = A and graduate year 2021")
print(college_df.loc[ (college_df.Age > 20) 
                            & (college_df.Grade == 'A') 
                                & (college_df.Graduate_Year == '2000') ,
                       ['Student_ID','First_Name','Age','Major', 'Graduate_Year']     
                    ] , "\n'")

print('..... 4(b) iloc() with conditions (single, multiple)')
# print(college_df.iloc[college_df.Major == 'Math']) generates Error
print(college_df.iloc[ list(college_df.Major == "Math")] , "\n") # all columns for students with the major in math
print(college_df.iloc[ list(college_df.Major == "Math") , : 3] , "\n") # columns from 0 to 3(excluede) for students with the major in math
print(college_df.iloc[ list(college_df.Major == "Math") , 3:] , "\n") # columns from 3 to then end for students with the major in math
print(college_df.iloc[ list(college_df.Age > 18) , 2:5] , "\n" ) # columns from 2 to 5(excluded) for students with Age>18
print(college_df.iloc[ list(college_df.Age > 18), :1] , "\n") #student ID for students with age>18


print()
print(">>>")
print(college_df.iloc[ list(college_df.Age > 25)], "\n")
print(college_df.iloc[ list(college_df.Grade == 'A')] , "\n")
print()
print('multiple conditions:')
print(college_df.iloc[ list((college_df.Major == "Math") 
                                &(college_df.Grade == 'A'))] , "\n")
# all columns for students with major in Math and grade=A

print(college_df.iloc[ list((college_df.Major == "Math") 
                                &(college_df.Grade == 'A')) , 
                                :3] , "\n")
# columns from 0 to 3(excluded) for students with major in Math and Grade = A

print('Student_ID for major in Math:')
print(college_df.iloc[ list((college_df.Major == "Math") 
                                &(college_df.Age > 18 )) , 
                                0] , "\n")
# column Student_ID for students with major in Math and Age>18

print("**************************************************************************")
print(' >>> 5) Selection Data via Callables ' , "\n")
print()
print('     5.a) loc() and callable/function:', "\n")
print(college_df.loc[ : , 
                       lambda college_df :['Last_Name'] ], "\n")
print(college_df.loc[ : , 
                       lambda college_df :['Last_Name','First_Name','Graduate_Year'] ], "\n")

print(College_DF.loc['Student_01':'Student_03'  , 
                        lambda College_DF :['LastName','Age']] , "\n" )

print(College_DF.loc['Student_01':'Student_04' ,
                        lambda College_DF : ['FirstName','Grade','GraduateYear']] , "\n")

# print(College_DF.loc['Student_02': , 
#                       lambda College_DF : ['LastName':'Grade']] , "\n") Error

# print(College_DF.loc['Student_02': , 
#                       lambda College_DF : ['LastName']] , "\n") Error

print(College_DF.loc['Student_02': , 
                      lambda College_DF : ['LastName','FirstName','GraduateYear']] , "\n") 

print(College_DF.loc['Student_02': , 
                      lambda College_DF : ['LastName','FirstName','GraduateYear']] , "\n") 

print(College_DF.loc[ lambda College_DF : ['Student_01','Student_02'] , 
                      : ], "\n") 

# print(College_DF.loc[ lambda College_DF :['Student_01':'Student_04'] ,
#                       ])
print('Initial College_DF')
print(College_DF)
print()

print(College_DF.loc[ lambda College_DF : College_DF.Age > '25' ,
                        :] , "\n")

print(College_DF.loc[ lambda College_DF : College_DF.GraduateYear > '2000' ,
                        :] , "\n")

print(College_DF.loc[ lambda College_DF : College_DF.Grade == 'A' ,
                        :] , "\n")

print(College_DF.loc[ lambda College_DF : College_DF.LastName == 'ONeil' ,
                        ['LastName','FirstName']] , "\n")

print(College_DF.loc[ lambda College_DF :['Student_01', 'Student_03'] ,
                                ['LastName','GraduateYear']], "\n")

#print(College_DF.loc[ lambda College_DF : ['Student_01':'Student:04'] , 
#                               ['LastName':'Grade']] , "\n") --> Invalid syntax

print(College_DF.loc[ lambda College_DF : ['Student_01','Student_03','Student_05'] , 
                                    : 'Age'] , "\n")

# print(College_DF.loc[ lambda College_DF : [:'Student_02'] , :]) --> Invalid syntax

# lambda for the rows:
print("lambda for the rows:--------------------")
# print(College_DF.loc[ : , lambda College_DF : ['LastName':'Age'] ] , "\n") invalid syntax 
print(College_DF.loc[ lambda College_DF : 'Student_01' , : ] , "\n")
print(College_DF.loc[ lambda College_DF : ['Student_02','Student_04' ] ] , "\n")
print(College_DF.loc[ lambda College_DF : ['Student_02','Student_04' ] , : ] , "\n")
# print(College_DF.loc[ lambda College_DF : ['Student_02':'Student_04']] , "\n") --> Invalid syntax
# print(College_DF.loc[ lambda College_DF : 'Grade'== 'A', : ]) --> Invalid syntax
print(College_DF.loc[ lambda College_DF : College_DF.Grade == 'A' , : ] , "\n")
print(College_DF.loc[ lambda College_DF : College_DF.LastName == 'Smith'] , "\n")
print(College_DF.loc[ lambda College_DF : College_DF.LastName == 'Smith' , : ] , "\n") # the same as the previous code line
print(College_DF.loc[ lambda College_DF : College_DF.Age > '18', 'LastName'] , "\n")
print(College_DF.loc[ lambda College_DF : College_DF.Age > '18', ['LastName','FirstName','Age'] ] , "\n")

# lambda for the column:
print("lambda for the column: ---------------------")
print("index for the students for all values of the column 'Grade' : ")
print(College_DF.loc[ : , lambda College_DF : 'Grade'] , "\n"  )
print(College_DF.loc[ : , lambda College_DF : ['LastName','GraduateYear'] ] , "\n")
print("First name of all students:")
print(College_DF.loc[ : , lambda College_DF : 'FirstName'] , "\n") # first name of all student
print("Graduate year for the student with Student_02 :")
print(College_DF.loc[ 'Student_02' , lambda College_DF:'GraduateYear'] , "\n") # graduate year for the student with index Student_02
# print(College_DF.loc['Student_02' , lambda College_DF : ['FirstName','Age'] , "\n"]) --> Indexing Error / too many indexers

print("      **********************************************************************")
print()
print('     5.b) iloc() and callable/function:', "\n")
print("- First and last name of the students with index 2 and 3 ( the indexes start with 0')")
print(College_DF.iloc[ lambda College_DF :[2,3] , : ] , "\n")

print ("- All columns for the last student/with index 4:")
print(College_DF.iloc[ lambda College_DF : [4] , :] , "\n")

print('- All columns for the students with age>30 :')
print(College_DF.iloc[ lambda College_DF : list(College_DF.Age > '30') , : ] , "\n")

print('- Students with the grade F')
print(College_DF.iloc[ lambda College_DF : list(College_DF.Grade == 'F'), : ] , "\n")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Section: Index", "\n")
student_dict = {
                'Student_ID': [10011,10022,10033,10044,10055] ,
                'Last_Name': ['Stephenson' , 'Pizaro' , 'Kim' , 'Williams' , 'Hua'] ,
                'First_Name': ['Grace', 'Maria', 'Lola', 'John' , 'Sofia'] ,
                'Age' : [22,30,27,19,45] ,
                'Grade' : ['B-','C','A','A','B'] , 
                'Graduate_Year' :[ '2021','2022','2000','2021','2021'] , 
                'Major' : ['Biology','Math','Art','Math','History']
               }



# create a DataFrame <student_info> with the default index column
student_info = pd.DataFrame(student_dict)
print(" * Data Frame <student_info> with the defaul index: ")
print(student_info , "\n")

# create a Data Frame <student_info2> and assign the column Student_ID as the index
student_info2 = pd.DataFrame(student_dict)
student_info2.set_index('Student_ID', inplace = True)
print(" * Data Frame <student_info2> with Student_ID columns as index: ")
print(student_info2 , "\n")

print(" * Data Frame <student_info3> with Last_Name columns as index: ")
student_info3 = pd.DataFrame(student_dict)
student_info3.set_index('Last_Name' , inplace = True)
print(student_info3, "\n")

print(' * Multiple columns as index')
student_info4 = pd.DataFrame(student_dict)
student_info4.set_index(['Last_Name','First_Name'] , inplace = True)
print(student_info4 , "\n")
print()

my_index = ['index0','index1','index2','index3', 'index4']
new_index = pd.Index(my_index)
student_info5 = pd.DataFrame(student_info)
student_info5.set_index(new_index , inplace = True)
print(student_info5 , "\n")

'''
print()
print(" 4) iloc() method") # retrieve values belonging to a row/column with a specific index
# iloc() function accepts only integer types values as index values




print('>>> the initial dataframe "college_df"')
print(college_df, "\n")

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




'''
