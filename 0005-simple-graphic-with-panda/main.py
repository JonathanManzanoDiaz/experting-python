import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
print(df.head())

plt.plot(df["dia"], df["ventas"], marker='o')
plt.title("Ventas por día")
plt.xlabel("dia")
plt.ylabel("ventas")
plt.savefig("grafica.png")
plt.show()
