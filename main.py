import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Netflix Dataset.csv')
# ['Show_Id', 'Category', 'Title', 'Director', 'Cast', 'Country',
#       'Release_Date', 'Rating', 'Duration', 'Type', 'Description']


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