import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Netflix Dataset.csv')
# ['Show_Id', 'Category', 'Title', 'Director', 'Cast', 'Country',
#       'Release_Date', 'Rating', 'Duration', 'Type', 'Description']

#10) What is the maximum duration of a Movie/Show on Netflix ?
# Extract minutes from duration strings for Movies
def get_minutes(duration_str):
    try:
        return int(duration_str.replace(' min', ''))
    except:
        return 0

# Find the maximum minutes for Movies
max_minutes = 0
for duration in df[df['Category'] == 'Movie']['Duration']:
    if 'min' in str(duration):
        minutes = get_minutes(duration)
        if minutes > max_minutes:
            max_minutes = minutes

print(f"Maximum duration of a Movie: {max_minutes} minutes")

# Show all movies with this maximum duration
longest_movies = []
for idx, row in df[df['Category'] == 'Movie'].iterrows():
    if 'min' in str(row['Duration']):
        minutes = get_minutes(row['Duration'])
        if minutes == max_minutes:
            longest_movies.append(row['Title'])

print(f"Movies with {max_minutes} minutes:")
for title in longest_movies:
    print(f"-  {title}")


# Find the maximum duration for TV Shows
tv_max_duration = df[df['Category'] == 'TV Show']['Duration'].max()
print(f"Maximum duration for TV Shows: {tv_max_duration}")

print(tv_max_duration)