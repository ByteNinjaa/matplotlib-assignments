import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plt.bar(top_teams_2010['Team Name'], top_teams_2010['Win Percentage'])
plt.title("Win Percentage of NHL Teams in 2010")
plt.xlabel("Team Name")
plt.xticks(rotation=45)  # Rotate team names for better visibility
plt.ylabel("Win Percentage")
plt.show()
