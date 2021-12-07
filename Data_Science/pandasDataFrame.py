import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("FinalProject.csv")
print(df.info())

df["total_major_championships"] = df["FIFA World Cup Wins (world championship by country)"] + df["Copa America OR Euro Cup Championships"]
print(df["total_major_championships"])
print(df.info())
df.plot.pie(y="Average Goals per Game", labels=df["Name"], title="Average Goals per Game", figsize=(12, 12))
plt.axis("off")
plt.show()
df["total_major_championships"].plot.hist(bins=5, color=["red"], title="Total Major Championships with National Team (World Cup, Copa America, Euro Cup)")
plt.show()
df.plot.scatter(x="Average Goals per Game", y="total_major_championships", subplots=True, color=["red"], title=["Total Major Championships with National Team vs Avg Goals per Game"])
plt.show()
