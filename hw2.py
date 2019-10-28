# Create a python module (a file with extension ‘.py’) with the following functions:

# (1 points) Write a python reads creates a dataframe from a URL that points to a CSV file such as the pronto data or CSVs in data.gov.

# (6 points) Create the function test_create_dataframe that takes as input:
# ((a) a pandas DataFrame and (b) a list of column names. The function returns
# (True if the following conditions hold:

# The DataFrame contains only the columns that you specified as the second argument.
# The values in each column have the same python type
# There are at least 10 rows in the DataFrame.

import pandas as pd

# write a function read csv file given URL
def read_url(url):
    return pd.read_csv(url)


# write fuction to test if the dataframe satisifies certain conditions
def test_create_dataframe(df,colName):
    # return true if all conditions satisfied
    # The DataFrame contains only the columns that you specified as the second argument.
    c1_colname = (list(df.columns.values) == colName)
    # The values in each column have the same python type
    type_list = []
    for i in range(len(df.columns)):
        columns  = df.iloc[:,i]
        type0 = type(columns[0])
        type_list.append(all(isinstance(columns[j],type0) for j in range(len(df))))

    c2_datatype = all(type_list)
    # There are at least 10 rows in the DataFrame.
    c3_rows = (len(df) >=10)

    return (c1_colname & c2_datatype & c3_rows)
    # if c1_colname & c2_datatype & c3_rows:
    #     return True
    # else:
    # 	return False
    		# print('data type check:', c2_datatype)
    		# print('row number check'. c3_rows))


