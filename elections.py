import pandas as pd
import numpy as np
filename = 'filename.csv'
election = pd.read_csv(filename, index_col='county')


results = election[['winner', 'total', 'voters']]

#print(election.head())
p_countries = election.loc['Potter':'Perry': -1]

prueba = election.iloc[5,3]
print(prueba)
print(p_countries)