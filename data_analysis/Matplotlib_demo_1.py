import pandas as pd
import matplotlib.pyplot as plt


unrate = pd.read_csv('unrate.csv')
print(unrate.shape)
print(unrate.head())

unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head())

first_twelve =  unrate[0:12]
plt.plot(first_twelve['DATE'],first_twelve['VALUE'])
plt.xticks(rotation = 45)
# print(help(plt.xticks))
plt.xlabel('Mouth')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends')
plt.show()
