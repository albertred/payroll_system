import pandas as pandas
from pandas import ExcelWriter
from pandas import ExcelFile
df = pandas.read_excel('Book.xlsx', sheet_name='Sheet1')

# print(df)
# print(df['Name'])
# print(df.at[0,'A'])

value = df.iloc[0]["Name"]
print(value)


