import pandas as pd

df = pd.read_csv('countries_with_missing_blood_group_values.csv')

# Вывод DataFrame
print(df.info())
print(df.describe())
print(df.head())
pass



df_salary = pd.read_csv('dz.csv')

# Проверка данных
print(df_salary.head())  # Вывод первых строк для проверки
print(df_salary.info())  # Информация о данных

# Группировка по городу и вычисление средней зарплаты
average_salary_by_city = df_salary.groupby('City')['Salary'].mean()

# Вывод результата
print(average_salary_by_city)
