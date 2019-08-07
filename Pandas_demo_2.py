import pandas as pd
import numpy as np

titanic_survival = pd.read_csv("titanic_train.csv")
print(titanic_survival.shape)
# print(titanic_survival.head())
# print(titanic_survival.columns)

# 分析年龄数据
age = titanic_survival["Age"]
print("年龄最大值：",age.max())
print("年龄最小值：",age.min())
age_is_null = pd.isnull(age)
# 用notnull获得有意义年龄
age_is_not_null = pd.notnull(age)
# 另一种循环获得游泳年龄
# ages_useful = titanic_survival["Age"][True!=age_is_null]

# 平均年龄 1
average_age_1 = sum(age[age_is_not_null])/len(age[age_is_not_null])
print("平均年龄：",average_age_1)

# 平均年龄 2
average_age_2 = titanic_survival["Age"].mean()
print("平均年龄：",average_age_2)

# Please pay attention to average age.
# Sometime there are lots of NaN in age's data.
# If we delete NaN data, we will lost import data.
# So we could replace NaN data by the average

# 处理另外一个数据Pclass
pclass = titanic_survival["Pclass"]
pclass_is_null = pd.isnull(pclass)

print("Pclass 最大值:",pclass.max())
print("Pclass 最小值:",pclass.min())
print("NaN值的个数为：",len(titanic_survival[pclass_is_null]))

# Method one:getting data and calculating average
# p_class = [1,2,3]
# pclass_fares_columns = ["Pclass","Fare"]
# pclass_fares=titanic_survival[pclass_fares_columns]
# aver_fare_class = {}
# for pclass in p_class:
#     pclass_each = pclass_fares[pclass_fares["Pclass"] == pclass]
#     average_fare_each = pclass_each["Fare"].mean()
#     aver_fare_class[pclass] = average_fare_each
# print(aver_fare_class)

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

# Using loc to show values by index and columns
row_index_83_age = titanic_survival.loc[83,"Age"]
row_index_1000_pclass = titanic_survival.loc[766,"Pclass"]

print(titanic_survival[766:767].T)