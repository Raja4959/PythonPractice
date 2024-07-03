# reading the two input files provided please print the following
# output::

# First Name  Last Name   Address Age  years of exp   Designation
# Jon         Tailor      US      45            21    Enterprise Architect
# Tom         Ok          GB      21             6    Dev
# Duke        Ok          GB      22             7    Tech Lead
# Harry       Ok          GB      23             8    Manager

# NOTE: idenx values to be omitted from the output

import pandas as pd

print("helllo")
col_file = open("columns.txt")
cols = col_file.read().splitlines()
# print(lines)

data = pd.read_csv("data.csv", names=cols)
data.reset_index(drop=True, inplace=True)
print(data)
# print(data.to_csv(index=False))
