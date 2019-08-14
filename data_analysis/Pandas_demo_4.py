import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')
fandango_films = fandango.set_index('FILM',drop = False)
# print(fandango_films.head())

print(fandango_films['Cinderella (2015)':'Hot Tub Time Machine 2 (2015)'])

