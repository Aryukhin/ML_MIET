import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('train.csv')

survived_age = df[df['Survived'] == 1]['Age'].dropna()
not_survived_age = df[df['Survived'] == 0]['Age'].dropna()

plt.hist([survived_age, not_survived_age], bins=20, label=['Выжившие', 'Не выжившие'], alpha=0.7, color=['green', 'red'])
plt.title('Гистограмма зависимости возраста от выживаемости')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.legend()

# Отображение гистограммы
plt.show()