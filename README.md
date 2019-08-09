# houchangxi.github.ai

## Andrew's Space
# Numpy 和 Pandas 数据清洗
   
# Method two: pivot_table is method to show the relationship between 2 data
p_fare = titanic_survival.pivot_table(index="Pclass", values="Fare", aggfunc=np.mean)
print(p_fare)

p_age = titanic_survival.pivot_table(index="Pclass", values="Age", aggfunc=np.mean)
print(p_age)

# Using different algorithms to calculate
em_fare_survived = titanic_survival.pivot_table(index="Embarked", values=["Fare","Survived"],aggfunc=np.sum)
print(em_fare_survived)

# Using dropna method to clean data
drop_na_columns = titanic_survival.dropna(axis=1)
titanic_survival_new_one = titanic_survival.dropna(axis=0,subset=["Age","Sex"])
print(titanic_survival_new_one.shape)


fandango = pd.read_csv("fandango_score_comparison.csv")
# We can see 3 type include DataFrame,Series and ndarray in Pandas data type.
To Summary, Pandas is base on numpy package :
Pandas <class 'pandas.core.frame.DataFrame'>
Series in Pandas <class 'pandas.core.series.Series'>
Items in Series <class 'numpy.ndarray'>


# We can use numpy to calculate series

1,
print(np.add(series_custom,series_custom))

2,
series_custom_more_than_50 = series_custom[series_custom>50]

3,
rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])

rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])

rt_mean = (rt_scores+rt_critics)/2



重点：
1、Python切记 注意事项
  
  a, 如果b的值设成a的初始化值，可以用 a = b.copy() 对a进行赋值。
  
  b, 浅层复制可以使用  a = b.View()  这种复制用 print(a is b)进行判断为Fasle 说明2个变量!=，并且用shape查看也为不同变量。但是若a中的数据变化则b中数   据也随之变化，故不建议使用这种浅层复制。
  
  注：赋值变量不用 "=" 用 "copy"。 “=” 如 a=b a、b指针相同，修改其中一个都会改变。 

2、常用Numpy 命令
   
   a, numpy.argmax     最大值索引
   
   b, numpy.tile       numpy.tile(data,(3,5)) 赋值data数据成为[3,5]的矩阵
   
   c, numpy.argsort    排序返回索引 （默认从小到大）
