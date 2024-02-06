import pandas as pd
df = pd.read_csv('train.csv')
val = df['Embarked'].value_counts()
df_surv = df[df['Survived'] == 1]
val_surv = df_surv['Embarked'].value_counts()
print(val_surv / val)