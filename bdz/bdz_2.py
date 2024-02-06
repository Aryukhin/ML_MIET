import pandas as pd
df = pd.read_csv('train.csv')
numeric_columns = df.select_dtypes(include='number')
res = df.groupby('Sex')[numeric_columns.columns].describe()
print(res)