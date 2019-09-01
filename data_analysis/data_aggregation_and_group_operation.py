import pandas as pd
import numpy as np




df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
print(df)
grouped = df['data1'].groupby(df['key1'])
print()
print(grouped.mean())
# Sometimes we need to use several column as index
grouped_1 = df['data1'].groupby([df['key1'],df['key2']])
means = grouped_1.mean()
print(means)
# Using hierarchical index
print(means.unstack())
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
print(df['data1'].groupby([states,years]).mean().unstack())
# directly using columns to group,
print(df.groupby('key1').mean())
print(df.groupby(['key1','key2']).mean())
# Using size()
print(df.groupby(['key1','key2']).size())

# Iterating Over Groups

for name,group in df.groupby('key1'):
    print(name)
    print()
    print(group)

for (k1,k2), group in df.groupby(['key1','key2']):
    print((k1,k2))
    print()
    print(group)

pieces = dict(list(df.groupby('key1')))
print()
print(pieces['a'])
print(df.dtypes)

grouped = df.groupby(df.dtypes,axis=1)
for dtype,group in grouped:
    print(dtype)
    print(group)

# Selecting a column or subset of columns

