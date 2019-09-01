import pandas as pd
import numpy as np

# Combining and Merging datasets

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
print(df1)
print()
print(df2)

print(pd.merge(df1,df2))
print(pd.merge(df1,df2,on='key'))

# 设定不同name的列进行merge
# 切记默认的merge 是用 how = 'inner'
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))

print(pd.merge(df1,df2,how='outer'))

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': range(5)})

print(df1)
print()
print(df2)

print(pd.merge(df1,df2,on='key',how='left'))
print(pd.merge(df1,df2,how='inner'))

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})

print(left)
print()
print(right)
print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))
print()
print(pd.merge(left,right,on='key1'))
print()
print(pd.merge(left,right,on='key1',suffixes=('_left','_right')))



