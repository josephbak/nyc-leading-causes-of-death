import pandas as pd


df = pd.read_csv('modified_nyc_deaths_final.csv')


print(df['Year'].unique())
# print(type(df['Year'].unique()))
print(sorted(list(df['Year'].unique())))