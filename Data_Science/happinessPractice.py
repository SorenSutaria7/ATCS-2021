import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", none)

df = pd.read_csv("../data/data.csv")
print(df.shape)
print(df.info())

print(df.describe())

df["support_to_life_expectancy"] = df["healthy_life_expectancy"] / df[""]
print(df["support_to_life_expectancy"])

print(df[["country", "GDP"]])

print(df.iloc[0:2, 3:7])
print(df.loc[df["country"] == "Ghana"])

df1 = df.groupby("continent").sum()
df1.plot.pie(y="perceptions_of_corruption", )