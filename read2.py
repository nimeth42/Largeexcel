import pandas as pd

excel_file = 'books.xlsx'
df = pd.read_excel(excel_file)

excel_file = 'books.xlsx'
df = pd.read_excel(excel_file)

print(df)
print(df.head(5))
print(df.tail(5))
print(df.index)
print(df.columns)
print(df.dtypes)