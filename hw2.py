# Create a python module (a file with extension ‘.py’) with the following functions:

# (1 points) Write a python reads creates a dataframe from a URL that points to a CSV file such as the pronto data or CSVs in data.gov.

# (6 points) Create the function test_create_dataframe that takes as input: (a) a pandas DataFrame and (b) a list of column names. The function returns True if the following conditions hold:

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
    # The values in each column have the same python type
    # There are at least 10 rows in the DataFrame.
    if (list(df.columns.values) == colName)  & len(set(df.dtypes.values.tolist())) == 1 & (len(df) >=10):
        return True 