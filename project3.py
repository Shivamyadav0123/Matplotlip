import pandas as pd
import matplotlib.pyplot as plt

data = {
    "City": ["Lucknow", "Delhi", "Mumbai", "Pune", "Jaipur",
             "Kanpur", "Bhopal", "Patna", "Noida", "Agra"],
    "Satisfaction_Score": [82, 74, 91, 88, 67, 79, 85, 62, 94, 71],
    "Complaints": [45, 78, 32, 39, 67, 51, 41, 82, 28, 63],
    "Customers": [450, 720, 850, 610, 390, 520, 480, 350, 680, 420]
}

df = pd.DataFrame(data)

# 1. City with highest satisfaction
best_city = df.loc[df["Satisfaction_Score"].idxmax()]
print("Highest Satisfaction City:", best_city["City"])
print("Satisfaction Score:", best_city["Satisfaction_Score"])

# 2. City with highest complaints
worst_complaints = df.loc[df["Complaints"].idxmax()]
print("\nHighest Complaints City:", worst_complaints["City"])
print("Complaints:", worst_complaints["Complaints"])

# 3. Average satisfaction
average = df["Satisfaction_Score"].mean()
print("\nAverage Satisfaction:", round(average, 2))

# 4. Sort cities in descending order
df_sorted = df.sort_values(
    by="Satisfaction_Score", ascending=False
)

# 5. Horizontal bar chart
plt.figure(figsize=(10, 6))

colors = [
    "green", "blue", "orange", "purple", "red",
    "cyan", "gold", "pink", "brown", "gray"
]

plt.barh(
    df_sorted["City"],
    df_sorted["Satisfaction_Score"],
    color=colors
)

# Highest score at the top
plt.gca().invert_yaxis()

plt.title("City-Wise Customer Satisfaction")
plt.xlabel("Satisfaction Score")
plt.ylabel("City")
plt.savefig("task3.png")

plt.xlim(0, 100)
plt.xticks(range(0, 101, 10))
plt.grid(axis="x", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.show()

# Conclusion
print("\nConclusion:")
print("Noida has the highest satisfaction score.")
print("Patna has the highest number of complaints.")