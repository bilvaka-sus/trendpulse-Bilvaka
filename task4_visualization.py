import pandas as pd

df = pd.read_csv("cleaned_trends.csv")
import matplotlib.pyplot as plt
df["category"].value_counts().plot(kind="bar")

plt.title("Number of Stories per Category")
plt.xlabel("Category")
plt.ylabel("Count")

plt.show()
top_scores = df.sort_values(by="score", ascending=False).head(10)

top_scores.plot(x="title", y="score", kind="bar")

plt.title("Top 10 Highest Scored Stories")
plt.xlabel("Story Title")
plt.ylabel("Score")

plt.xticks(rotation=45)

plt.show()
df["num_comments"].plot(kind="hist")

plt.title("Distribution of Comments")
plt.xlabel("Number of Comments")

plt.show()
plt.savefig("graph.png")
