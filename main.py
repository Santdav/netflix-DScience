import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Netflix Dataset.csv')

##print(df.columns)

hoc = df[df["Title"]=="House of Cards"]

print(hoc[["Show_Id","Title","Director"]])