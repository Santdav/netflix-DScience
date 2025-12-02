import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Netflix Dataset.csv')
# ['Show_Id', 'Category', 'Title', 'Director', 'Cast', 'Country',
#       'Release_Date', 'Rating', 'Duration', 'Type', 'Description']

#Q. 7) Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".
result = df[((df['Category'] == 'Movie') & (df['Type'] == 'Comedies')) | (df['Country'].str.contains('United Kingdom', na=False))]
print(result)