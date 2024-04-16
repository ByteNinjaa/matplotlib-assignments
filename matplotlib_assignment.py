import pandas as pd
import matplotlib.pyplot as plt

file_path = "student_scores.csv"

df = pd.read_csv(file_path)
dfbp = df.boxplot(patch_artist=True)

colors = ['blue', 'green', 'red']
for box, color in zip(dfbp.artists, colors):
    box.set_facecolor(color)

plt.savefig("customized_box_plot.png")
plt.show()
