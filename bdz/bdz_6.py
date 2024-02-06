import pandas as pd
df = pd.read_csv('train.csv')
df1 = pd.read_csv('test.csv')

correlation_matrix = df.corr()['Survived']
print(correlation_matrix)