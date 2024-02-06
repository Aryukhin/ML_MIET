import pandas as pd
df = pd.read_csv('train.csv')
numeric_columns = df.select_dtypes(include='number')
for column in numeric_columns:
    median_value = numeric_columns[column].median()
    numeric_columns[column].fillna(median_value, inplace=True)
missing_values = numeric_columns.isnull().any()
print(f'Пустые значения:{missing_values}')