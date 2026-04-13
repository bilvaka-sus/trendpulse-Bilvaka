# Task 3
data analysis
import pandas as pd

df = pd.read_csv("cleaned_trends.csv")
loading my CSV
df.head()
previewing again
df["category"].value_counts()
count stories per category
df["score"].mean()
average score
df["num_comments"].mean()
average comments
df.sort_values(by= "score", ascending=False).head(5)
top 5 highest scored posts
df["author"].value_counts().head(5)
most active authors
df.groupby("category")["score"].mean()
