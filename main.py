import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Netflix Dataset.csv')
# ['Show_Id', 'Category', 'Title', 'Director', 'Cast', 'Country',
#       'Release_Date', 'Rating', 'Duration', 'Type', 'Description']

movies_2000 = df[(df['Category'] == 'Movie') & (df['Release_Year'] == 2000)]

print("Movies released in 2000:")
for title in movies_2000['Title']:
    print(f"-  {title}")