# Series

import pandas as pd
from pandas import Series
import numpy as np


fandango = pd.read_csv("fandango_score_comparison.csv")
print(type(fandango))
# print(fandango.columns)

series_film = fandango["FILM"]
print(type(series_film))
series_rt = fandango['RottenTomatoes'];
# print(series_film[0:6])

frim_names = series_film.values
# print(frim_names)
rt_scores = series_rt.values
print(type(rt_scores))

# From data's type below, we can see 3 type include DataFrame Series ndarray.
# To Summary, Pandas is base on numpy package
# <class 'pandas.core.frame.DataFrame'>
# <class 'pandas.core.series.Series'>
# <class 'numpy.ndarray'>


series_custom = Series(rt_scores,index=series_film)
# print(series_custom[['Minions (2015)','Leviathan (2014)']])
# print(series_custom[5:8])

#reindex
original_index = series_custom.index.tolist()
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)
print(sorted_by_index.head())

# sort
sc_ind = series_custom.sort_index()
sc_val = series_custom.sort_values()
print(sc_ind[0:2])
print(sc_val[0:2])



# we can use numpy to calculate series
# print(np.add(series_custom,series_custom))
print(np.max(series_custom))

series_custom_more_than_50 = series_custom[series_custom>50]
print(series_custom_more_than_50.head())

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_scores+rt_critics)/2
print(rt_mean[0:5])
