#Soren Sutaria
#Eminem Final Project ATCS 2021 Block F
#Data Science Visualizations

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Setting the theme from seaborn
sb.set_theme()

#Reading in the data
df = pd.read_csv("FinalData.csv")
print(df.dtypes)

#Creating a pie chart that seperates the genres of the nominations
#Only nominated values, includes winners
dataNominations = df.loc[df["Nominated"] == True]
genres = dataNominations.groupby("Genre").count()
colors = sb.color_palette('pastel')[0:6]
genres.plot.pie(y="Year", colors=colors, title="Genre of All Nominated", autopct='%.0f%%')
plt.show()

#Creating a pie chart that seperates the genres of the winners
#Only winner values
dataWinners = df.loc[df["Winner"] == True]
genresWinners = dataWinners.groupby("Genre").count()
genresWinners.plot.pie(y="Year", colors=colors, title="Genre of Winners",  autopct='%.0f%%')
plt.show()

#Comparing Spotify Streams vs Album Global Sales for all the albums
dataNominations = df.loc[df["Nominated"] == True]
ax = sb.regplot(x="Album Global Sales", y="Spotify Streams", data=dataNominations)
plt.show()

#Creating a data set of only eminem and the wwinners and comparing their CSPC
dataWinnersAndEminem = df.loc[df["Compare"] == True]
print(dataWinnersAndEminem)
ax = sb.barplot(x="Artist", y="CSPC", hue="Winner", data=dataWinnersAndEminem)
plt.show()

#Creating two bar plots comparing the nominations of 2000 for global sales and spotify streams
data2000s = df.loc[df["Year"] == 2000]
ax = sb.barplot(x="Album", y="Album Global Sales", hue="Winner", data=data2000s)
plt.show()
ax = sb.barplot(x="Album", y="Spotify Streams", hue="Winner", data=data2000s)
plt.show()

#Creating two bar plots comparing the nominations of 2001 for global sales and spotify streams
data2001 = df.loc[df["Year"] == 2001]
ax = sb.barplot(x="Album", y="Album Global Sales", hue="Winner", data=data2001)
plt.show()

#Creating two bar plots comparing the nominations of 2003 for global sales and spotify streams
data2003 = df.loc[df["Year"] == 2003]
ax = sb.barplot(x="Album", y="Album Global Sales", hue="Winner", data=data2003)
plt.show()
ax = sb.barplot(x="Album", y="Spotify Streams", hue="Winner", data=data2003)
plt.show()

#Creating two bar plots comparing the nominations of 2006 for global sales and spotify streams
data2006 = df.loc[df["Year"] == 2006]
ax = sb.barplot(x="Album", y="Album Global Sales", hue="Winner", data=data2006)
plt.show()
ax = sb.barplot(x="Album", y="Spotify Streams", hue="Winner", data=data2006)
plt.show()

#Creating two bar plots comparing the nominations of 2011 for global sales and spotify streams
data2011 = df.loc[df["Year"] == 2011]
ax = sb.barplot(x="Album", y="Album Global Sales", hue="Winner", data=data2011)
plt.show()
ax = sb.barplot(x="Album", y="Spotify Streams", hue="Winner", data=data2011)
plt.show()

#Creating two bar plots comparing the nominations of 2015 for global sales and spotify streams
data2015 = df.loc[df["Year"] == 2015]
ax = sb.barplot(x="Album", y="Album Global Sales", hue="Winner", data=data2015)
plt.show()
ax = sb.barplot(x="Album", y="Spotify Streams", hue="Winner", data=data2015)
plt.show()
