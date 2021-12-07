import pandas as pd
import matplotlib.pyplot as plt

goalsPerGame = pd.Series([0.9384, 0.563, 0.8043, 0.7315, 0.6721, 0.1943, 0.58, 0.1307], index=["Pele", "Maradona", "Messi", "C. Ronaldo", "Ronaldo L.", "Zidane", "Cruyff", "Beckenbauer"])

plt.boxplot(goalsPerGame)
plt.show()