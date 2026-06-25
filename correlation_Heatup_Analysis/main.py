import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read dataset
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "students.csv")

df = pd.read_csv(csv_path)

# Correlation matrix
corr = df.corr()

print("Correlation Matrix:")
print(corr)

# Heatmap
plt.figure(figsize=(6,5))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()

# Pairplot
pair = sns.pairplot(df)

# Add title
pair.fig.suptitle("Pairwise Relationships", y=1.02)

# Save pairplot
pair.savefig("pairplot.png")

# Show pairplot
plt.show()

print("Pairplot saved successfully!")

print("Heatmap and Pairplot saved successfully.")
