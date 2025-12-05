So we load first

```python
df = pd.read_csv('Netflix Dataset.csv')
```
This dataset had the following promts to answer


Q. 1) For 'House of Cards', what is the Show Id and Who is the Director of this show ?
```python
hoc = df[df["Title"]=="House of Cards"]
print(hoc[["Show_Id","Title","Director"]])
```

Q. 2) In which year the highest number of the TV Shows & Movies were released ? Show with Bar Graph.
```python
# Format to years
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')
df['Release_Year'] = df['Release_Date'].dt.year

## Count releases per year
yearly_counts = df['Release_Year'].value_counts().sort_index()
max_year = yearly_counts.idxmax()
max_count = yearly_counts.max()

# logging the result
print(f"Year with highest number of releases: {max_year}")
print(f"Number of releases in {max_year}: {max_count}")



plt.figure(figsize=(12, 9))
bars = plt.bar(yearly_counts.index.astype(str), yearly_counts.values)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{int(height)}', ha='center', va='bottom', fontsize=9)

# Add labels and title
plt.title('Number of TV Shows & Movies Released by Year', fontsize=16, fontweight='bold')
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Number of Releases', fontsize=12)
plt.xticks(rotation=25, ha='right')
# Add gridlines for better readability
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

Q. 3) How many Movies & TV Shows are in the dataset ? Show with Bar Graph.
```python
# get counts of each category
category_counts = df['Category'].value_counts()

# Logging the results
print("Total number of Movies & TV Shows in the dataset:")
print(f"Total entries: {len(df)}")
print("\nBreakdown by Category:")
print(f"Movies: {category_counts.get('Movie', 0)}")
print(f"TV Shows: {category_counts.get('TV Show', 0)}")

# Visualization
plt.figure(figsize=(8,6))

bars = plt.bar(category_counts.index, category_counts.values, 
               color=['blue', 'orange'], width=0.6)
plt.title('Movies vs TV Shows', fontsize=14, fontweight='bold')
plt.xlabel('Type', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(axis='y', alpha=0.3)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), 
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
```

Q. 4) Show all the Movies that were released in year 2000.
```python
movies_2000 = df[(df['Category'] == 'Movie') & (df['Release_Year'] == 2000)]

print("Movies released in 2000:")
for title in movies_2000['Title']:
    print(f"-  {title}")
```

Q. 5) Show only the Titles of all TV Shows that were released in India only.
```python

indiaTvShows = df[(df['Category'] == 'TV Show') & (df['Country'] == 'India')]
# equally comparator filder only "India"

print(f"\nTotal TV Shows released in India: {len(indiaTvShows)}")
for title in indiaTvShows['Title'].tolist():
    print(title)
```

Q. 6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?
```python
#6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ? with number of TV Shows & Movies also.
top_directors = df['Director'].value_counts().head(10)
print("Top 10 Directors with the highest number of TV Shows & Movies on Netflix:")
print(top_directors)
```

Q. 7) Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".
```python
result = df[((df['Category'] == 'Movie') & (df['Type'] == 'Comedies')) | (df['Country'].str.contains('United Kingdom', na=False))]
print(result)
```

Q. 8) In how many movies/shows, Tom Cruise was cast ?
```python
Tcruise_roles = df[df['Cast'].str.contains('Tom Cruise', na=False)]
print(f'Tom Cruise was cast in {Tcruise_roles["Title"].count()} movies/shows.')
```

Q. 9) What are the different Ratings defined by Netflix ?
```python
ratings = df['Rating'].unique()
print("Different Ratings defined by Netflix:")
print(ratings)

```
- Q. 9.1) How many Movies got the 'TV-14' rating, in Canada ?
  ```python
    movies_tv14_canada = df[(df['Rating'] == 'TV-14') & (df['Country'] == 'Canada') & (df['Category'] == 'Movie')]
    print(f"Number of Movies with 'TV-14' rating in Canada: {movies_tv14_canada.shape[0]}")
  ```
- Q. 9.2) How many TV Shows got the 'R' rating, after year 2018 ?
  ```python
    # Convert Release_Date to datetime and extract year
    df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')
    df['Release_Year'] = df['Release_Date'].dt.year

    # Count TV Shows with 'R' rating after 2018
    count = len(df[(df['Category'] == 'TV Show') & 
               (df['Rating'] == 'R') & 
               (df['Release_Year'] > 2018)])

    print(f"Number of TV Shows with 'R' rating after 2018: {count}")
  ```

Q. 10) What is the maximum duration of a Movie/Show on Netflix ?
```python
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
```

Q. 11) Which individual country has the Highest No. of TV Shows ?

Q. 12) How can we sort the dataset by Year ?

Q. 13) Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'.