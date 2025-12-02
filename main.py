import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Netflix Dataset.csv')
# ['Show_Id', 'Category', 'Title', 'Director', 'Cast', 'Country',
#       'Release_Date', 'Rating', 'Duration', 'Type', 'Description']


indiaTvShows = df[(df['Category'] == 'TV Show') & (df['Country'] == 'India')]

print(f"\nTotal TV Shows released in India: {len(indiaTvShows)}")
for title in indiaTvShows['Title'].tolist():
    print(title)