import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('Study_vs_Score_data.csv')
# print(df.head())

x = df["Attendance_Hours"]
y = df["Final_Marks"]

a, b, r, p, erro = linregress(x, y)

print(f"Coeficiente angular: {a:.2f}")
print(f"Intercepto: {b:.2f}")
print(f"Correlação: {r:.2f}")

reta = a * x + b

plt.scatter(x, y, label="Dados")
plt.plot(x, reta, color="red", label="Reta")

plt.title("Regressão Linear")
plt.xlabel("Attendance Hours")
plt.ylabel("Final Marks")
plt.legend()

print(f"\nEquação da reta:")
print(f"y = {a:.4f}x + {b:.4f}")

plt.show()