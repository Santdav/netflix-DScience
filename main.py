import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Netflix Dataset.csv')
# ['Show_Id', 'Category', 'Title', 'Director', 'Cast', 'Country',
#       'Release_Date', 'Rating', 'Duration', 'Type', 'Description']

#How many TV Shows got the 'R' rating, after year 2018 ?
# Convert Release_Date to datetime and extract year
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')
df['Release_Year'] = df['Release_Date'].dt.year

# Count TV Shows with 'R' rating after 2018
count = len(df[(df['Category'] == 'TV Show') & 
               (df['Rating'] == 'R') & 
               (df['Release_Year'] > 2018)])

print(f"Number of TV Shows with 'R' rating after 2018: {count}")