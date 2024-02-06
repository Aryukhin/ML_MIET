import pandas as pd
df = pd.read_csv('train.csv')
a = df.groupby(['Pclass', 'Sex', 'Survived'])['Survived'].agg('count')
print(a)