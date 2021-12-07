import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("swimTimes.csv")

x = df["year"]
y = df["seconds"]

correlation = y.corr(x)
print(correlation)

plt.title("Swim Times over the Years")
plt.xlabel("Year")
plt.ylabel("Time (seconds)")
plt.scatter(x, y)

model = np.polyfit(x, y, 1)
x_lin_reg = range(x.min(), x.max())

predict = np.poly1d(model)
y_lin_reg = predict(x_lin_reg)

plt.plot(x_lin_reg, y_lin_reg, color="red")
plt.show()