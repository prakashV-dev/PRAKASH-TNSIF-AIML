import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Alice","Bob","Charlie","David","Eva","Frank","Grace","Hannah","Ian","Jack"],
    "Marks": [85, 92, 58, 35, 74, 62, 45, 90, 38, 79],
}

df = pd.DataFrame(data)

def categorize_marks(mark):
    if mark >= 80:
        return "Excellent (80–100)"
    elif mark >= 60:
        return "Good (60–79)"
    elif mark >= 40:
        return "Average (40–59)"
    else:
        return "Needs Improvement (<40)"


df["Category"] = df["Marks"].apply(categorize_marks)
print("--- Student Dataset ---")
print(df)

plt.figure(figsize=(9, 5))
plt.bar(df["Student"],df["Marks"],color="mediumseagreen",edgecolor="black",label="Student Marks")
plt.axhline(y=40, color="red", linestyle="--", linewidth=1.5, label="Passing Mark (40)")

plt.title("Student Marks in Python", fontsize=14)
plt.xlabel("Student Name", fontsize=12)
plt.ylabel("Marks", fontsize=12)
plt.ylim(0, 100)
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.show()

category_counts = df["Category"].value_counts()
colors = ["#66b3ff", "#99ff99", "#ffcc99", "#ff9999"]

plt.figure(figsize=(7, 7))
plt.pie(category_counts,labels=category_counts.index,autopct="%1.1f%%",startangle=140,colors=colors,)

plt.title("Distribution of Performance Categories", fontsize=14)
plt.tight_layout()
plt.show()
