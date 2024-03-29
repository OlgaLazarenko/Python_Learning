
# Python_Learning

The purpose of this project is to practice and enhnace my skills at Python Pandas.
The project consists of several parts each of them is dedicated to a specific topic.
Each part has its own list of goals.

## PYTHON_PANDAS / Series, DataFrame       ----------------------------------------------------
### Series
- [x] create an empty series
- [x] create a series from a list with default/ and customized index
- [x] create a series from a dict with index 
- [] create a series from scalar, provide an index
- [x] access data  from series with position (iloc[] method)
- [x] access data from series using label (loc [] methond)
- [x] sort the dataframe asc/desc, by multiple columns 
- [x] sort the dataframe by multiple columns but different orders


- [x] compute summary statistics
- [x] compute the correlation
- [x] compute the numerical data ranks
- [] create plotting with Matplotlib


### DataFrame
## Section: DataFrame functions/

# *** Create a new job for Python Pandas "General Functions"
# Data manipulations
- [] access a single value in a data frame or series using a row/column label pair / pandas.DataFrame.at()
- [] access a group of rows and columns by label(s) / pandas.DataFrame.loc()
- [] melt
- [] pivot
- [] pivot_table
- [] crosstab
- [] cut
- [] qcut
- [] merge(left, right[, how, on, left_on])
- [] merge_ordered (left, right[,on, left_on])
- [] merge_asof
- [] concat
- [] get_dummies
- [] factorize
- [] unique
# Top-level missing data
- [] isna()
- [] isnull()
- [] notna()
- [] notnull()

# Top-level conversions
- [] to-numeric()

# Top-level dealing with datetimelike
- [] to_datetiem()
- [] to_timedalta()
- [] date_range()
- [] bdate_range()
- [] period_range()
- [] timedelta_range()
- [] inter_freq()

# Top-level dealinign with intervals
- [] interval_range()

# Top-level evaluation
- [] eval()

# Hashing ?
- [] util.hash_array()
- [] util.hash_pandas_object()

# Testing
- [] test()

# *** Create a new job for Pathon Pandas "DataFrame Functions" / most common



## Section: Python_Numpy
- [] plot the data from .csv file (single graph)
- [] plot the data from .csv file (multiple graphs)
- [] plot the data from .csv file (skip the header)


## Section: Python_Matplotlib
-[] plot the dasta from csv file(singtle and multiple plots)
-[] create different types of plots(line, bar chart, area, pie, scatter 3D plot, histogram)
-[] create plotes with customized features(color, legend, markers, scale)

##  Section: Axes Operations on DataFrame 
- [x] operations (mean, min, max) on dataframe when axis = 0 
- [x] operations (mean, min, max) on dataframe whenk axiz = 1
- [] combine dataframes when axis = 0
- [] combine dataframes when axis = 1

## Section: Filter DataFrame
- [x] 1) dataframe way to filter a dataframe

- [x] 2) query function to filter a dataframe
    - [x] 2.1) one column/condition
    - [x] 2.2) multiple columns/conditions
    - [x] 2.3) reference method 
    - [x] 2.4) pass variables in query function
    - [x] 2.5) features inplace = False/True

- [x] 3) loc() function


- [x] 4) iloc() function
- [x] 5) filer dataframe by row and column position
- [x] 6) select rows whose column value != a specific value
- []  7) negate a column
- []  5) select non-missing values in data frame
- []  6) filter string in DataFrame
- []  7) filter if a column name has a space

## Section:  Dataframe Index
indexing => selecting some rows/columns
Types of indexing (indexers):
1) -[] dataframe[] => indexing operator
        - [X] retrieve one column
        - [X] select multiple columns

2) -[] dataframe.loc[] => loc[] indexer => rows/columns labels/names
        a) [] index/label value
        b) [] list of labels
        c) [] logical/boolean index
        d) [] multiple condtions

3) -[] dataframe.iloc[] => iloc[] indexer => rows/columns position/integer

4) -[x] selecting data via conditions and callable
        a) -[x] loc() with conditions (single, multiple)
        b) - [x] iloc() with conditions (single, mulitple)
5) -[x] selecting data via callable/function
        a) - [x] loc() with callable/s
        b) - [x] iloc() with callable/s
        
6) -[] dataframe .ix[] => ix[] indexer => both: labels/names and position/integer

7) -[] retrieve data using list of labels
        a) loc()
        b) iloc()
## Section: Index 
- [x] default index 
- [x] set a column as index
- [x] set multi-index
- [] drop index column





