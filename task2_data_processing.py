task 2
taking JSON file -> clean it -> save as CSV

at first i actually tired to open a non-notebook file as a notbook then i created a new notebook and uploaded json by one code then it was loaded
from google.colab import files
uploaded = files.upload()
import pandas as pd

df = pd.read_json("trends_20260408.json")
import os
print(os.listdir())
this actually shows the exact file name
df.head()
we will see first 5 rows
df.info()
this tells how many rows, columns, missing values.
df.isnull().sum()
shows how many empty values in each column
sf = df.dropna(subset=["title"])
this removes rows with no title
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)
fill missing numbers
df = df.drop_duplicates(subset=["post_id"])
remmoves duplicates
df.to_csv("cleaned_trends.csv", index=False)
saved as a clean CSV
from google.colab import files
files.download("cleaned_trends.csv")
downloaded and final output as cleaned_trends.csv
