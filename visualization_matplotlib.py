import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(team_trend['Year'], team_trend['Win Percentage'], marker='o')
plt.title("Calgary Flames - Win Percentage Over Years")
plt.xlabel("Year")
plt.ylabel("Win Percentage")
plt.grid(True)
plt.show()
