import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Netflix Dataset.csv')
# ['Show_Id', 'Category', 'Title', 'Director', 'Cast', 'Country',
#       'Release_Date', 'Rating', 'Duration', 'Type', 'Description']

#Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'.
movies_dramas = df[(df['Category'] == 'Movie') & (df['Type'] == 'Dramas')]
tvshows_kids = df[(df['Category'] == 'TV Show') & (df['Type'] == 'Kids TV')]
result = pd.concat([movies_dramas, tvshows_kids])
print(result)