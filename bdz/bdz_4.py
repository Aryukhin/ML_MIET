import pandas as pd
from collections import Counter
df = pd.read_csv('train.csv')
name = df['Name'].apply(lambda x: x.split())
first_name = []
second_name = []
for i in name:
    first_name.append(i[2])
    second_name.append(i[0][:-1])
print(Counter(first_name).most_common(10))
print(Counter(second_name).most_common(10))