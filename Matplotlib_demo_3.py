import  pandas as pd

reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm','Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue','Fandango_Stars']
norm_reviews = reviews[cols]

print(norm_reviews[:1])