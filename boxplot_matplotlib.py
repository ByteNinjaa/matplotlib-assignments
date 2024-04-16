import matplotlib.pyplot as plt

subjects = ['Math', 'English', 'Science', 'History']
scores = [data[subject].values for subject in subjects]

plt.figure(figsize=(10, 6))
plt.boxplot(scores, labels=subjects)
plt.title('Student Performance in Different Subjects')
plt.ylabel('Scores')
plt.xlabel('Subjects')
plt.grid(True)
plt.show()
