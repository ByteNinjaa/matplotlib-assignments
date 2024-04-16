import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(df_hockey['Goals For'], df_hockey['Goals Against'], c=df_hockey['Goal Differential'], cmap='coolwarm', s=100)
plt.colorbar(label='Goal Differential')
plt.title("Goal For vs. Goal Against (Colored by Goal Differential)")
plt.xlabel("Goals For")
plt.ylabel("Goals Against")
plt.grid(True)
plt.show()
