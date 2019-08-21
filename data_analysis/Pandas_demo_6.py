# Data Cleaning and Preparation
# <Python for Data Analysis> Chapter 7 Page 191 to 221
import pandas as pd
import numpy as np
string_data  =  pd.Series(['aardvark','artichoke',np.nan,'avocado'])
print(string_data.isnull())

string_data[0]=None
print(string_data.isnull())

from numpy import nan as NA

data = pd.Series([1,NA,3.5,NA,7])
print(data)
print(data.dropna())
print(data.notnull())


data_p = pd.DataFrame([[1,6.5,3],[1,NA,NA],[NA,NA,NA],[NA,6.5,3]])
cleaned  = data_p.dropna()
print(data_p)
print()
print(cleaned)

# 删除所有都是 nan的值 用 how='all'
print()
print(data_p.dropna(how = 'all'))
# 删除某一列
data_p[4] = NA
print()
print(data_p)
print(data_p.dropna(axis=1,how='all'))

# df = pd.DataFrame(np.random.randint(1,10,(7,3)))
df = pd.DataFrame(np.random.randn(7,3))
df.iloc[:4,1] = NA
df.iloc[:2,2] = NA
print(df)
print()
print(df.dropna())
print()
print(df.fillna(0))
print()
print(df.fillna({1:0.5,2:0}))
print()
# make a new object
_a = df.fillna(0,inplace=True)
print(df)
print()
print(_a)

# method : {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, 默认值 None ; 在Series中使用方法填充空白（‘backfill’, ‘bfill’向前填充，‘pad’, ‘ffill’向后填充）
# limit 填写需要添加的行数 axis: row or column  inplace: true false
df = pd.DataFrame(np.random.randn(6,3))
df.iloc[-4:,1] = NA
df.iloc[-2:,2] = NA
print()
print(df)
print()
print(df.fillna(method='ffill'))
print()
print(df.fillna(method='ffill',limit=1))

# duplicated whether each row is a duplicate or not

data = pd.DataFrame({'k1':['one','two']*3 + ['two']+['one'],'k2':[1,1,2,3,3,4,4,1]})
print(data)
print(data.duplicated())
print(data.drop_duplicates())

data['v1'] = range(8)
print(data)
# 可以指定删除某一列的重复值
print(data.drop_duplicates(['k1']))
# 可以指定列去重 并保留最新的
print(data.drop_duplicates(['k1','k2'],keep='last'))

# food进行小写处理，再通过map获取值，对data进行列匹配
data = pd.DataFrame({'food':['bacon','pulled pork','bacon','Pastrami','corned beef','Bacon','pastrami','honey ham','nova lox'],'ounces':[4,3,12,6,7.5,8,3,5,6]})
print(data)
meat_to_animal = {'bacon':'pig','pulled pork':'pig','pastrami':'cow','corned beef':'cow','honey ham':'pig','nova lox':'salmon'}
lowercased = data['food'].str.lower()
print()
print(lowercased)
# 通过map取值
data['animal']=lowercased.map(meat_to_animal)
print(data)
print('++++++++',data['food'].map(lambda x : meat_to_animal[x.lower()]))

# Replacing Values
data_ = pd.Series([1.,-999.,2.,-999.,-1000.,3.,])
print(data_)
print()
print(data_.replace(-999,np.nan))
print(data_.replace([-999,-1000],np.nan))
print(data_.replace([-999,-1000],[np.nan,0]))
print(data_.replace({-999:np.nan,-1000:0}))

# Renaming Axis Indexes

data = pd.DataFrame(np.arange(12).reshape((3,4)), index=['Ohio','Colorado','New York'],columns=['one','two','three','four'])
print(data)
print()
transform = lambda x:x[:4].upper()
print(data.index.map(transform))

data.index = data.index.map(transform)
print(data)
print()
print(data.rename(index=str.title,columns=str.upper))
print(data.rename(index={'OHIO':'INDIANA'},columns={'three':'peekaboo'}))
data.rename(index={'OHIO':'INDIANA'},inplace=True)
print()
print(data)

# Discretization and Binning

ages = [20,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100]
cats = pd.cut(ages,bins)
print(cats)
print()
# cats's categories could be replace by labeling for the age data in the codes attribute
# we can operate cats.codes to discretizate data
print(cats.codes)
print(cats.categories)
# pandas.value_counts could be use to get the number of each categories
print(pd.value_counts(cats))
# Note that pd.value_counts are the bin count for the result of pd.cut
print(pd.cut(ages,[18,26,36,61,100],right=False))

group_names = ['Youth','YoungAdult','MiddleAged','Senior']
cats_2 = pd.cut(ages,bins,labels=group_names)
print(cats_2.codes)

data = np.random.rand(20)

print(pd.cut(data,4,precision = 2))
# The pd.cut and pd.qcut are different. please pay attention to both different
# cut based on the minimum and maximum values in the data,
# Consider the case of some uniformly distributed data chopped into fourths
# Since qcut uses sample quantiles instead, by definition you will obtain roughly equal-size bins
data = np.random.randn(1000)
cats = pd.qcut(data,4)
print(cats)
print(pd.value_counts(cats))
# You can pass your own quantiles (numbers between 0 and 1, inclusive)
print(pd.qcut(data,[0,0.25,0.5,0.75,1.]))

# Detecting and Filtering Outliers
data = pd.DataFrame(np.random.randn(1000,4))
print(data.describe())
col = data[2]

print(col[np.abs(col)>3])
print(data[(np.abs(data)>3).any(1)])

data[np.abs(data)>3] = np.sign(data)*3
print(data.describe())

# The statement np.sign(data) produces 1 and -1 values based on whether the values in data are positive or negative
print(np.sign(data).head())

# Permutation and Random Sampling
df = pd.DataFrame(np.arange(5*4).reshape((5,4)))
sampler = np.random.permutation(5)
print(sampler)
print()
print(df)
print(df.take(sampler))
print(df.sample(3))
choices = pd.Series([5,7,-1,6,4])
draws = choices.sample(n=10, replace=True)
print(draws)

# Computing Indicator/Dummy Variables  有一个demo分析 这步处理可以认为是one hot的手动数据处理
df = pd.DataFrame({'keys':['b','b','a','c','a','b'],'data1':range(6)})
print(pd.get_dummies(df['keys']))
dummies = pd.get_dummies(df['keys'],prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)
# 电影demo 完成数据处理 one hot 处理数据
mnames = ['movie_id','title','genres']
movies = pd.read_table('movies.dat',sep='::',header=None,names=mnames,engine='python')
print(movies.head())

all_genies = []
for cell in movies.genres:
    all_genies.extend(cell.split('|'))
# print(all_genies)
genies = pd.unique(all_genies)
print(genies)

zero_matrix = np.zeros((len(movies),len(genies)))
dummies = pd.DataFrame(zero_matrix,columns=genies)
# how to get each genies feature's index
gen = movies.genres[0]
print(gen)
print(gen.split('|'))
print(dummies.columns.get_indexer(gen.split('|')))

for i,gen in enumerate(movies.genres):
    index = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i,index] = 1
print(dummies.head())
# add into movies list
movies_windic = movies.join(dummies.add_prefix('Genre_'))
print(movies_windic.iloc[0])
# 总结上边的数据处理：速度慢 不适合数据量巨大的数据处理
# 可用dissertation function：cut 去对数据进行get_dummies

np.random.seed(3732)
values = np.random.rand(10)
bins= [0.,0.2,0.4,0.6,0.8,1.]
print(pd.get_dummies(pd.cut(values,bins)))
