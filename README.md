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

Q. 4) Show all the Movies that were released in year 2000.

Q. 5) Show only the Titles of all TV Shows that were released in India only.

Q. 6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?

Q. 7) Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".

Q. 8) In how many movies/shows, Tom Cruise was cast ?

Q. 9) What are the different Ratings defined by Netflix ?
Q. 9.1) How many Movies got the 'TV-14' rating, in Canada ?
Q. 9.2) How many TV Shows got the 'R' rating, after year 2018 ?

Q. 10) What is the maximum duration of a Movie/Show on Netflix ?

Q. 11) Which individual country has the Highest No. of TV Shows ?

Q. 12) How can we sort the dataset by Year ?

Q. 13) Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'.