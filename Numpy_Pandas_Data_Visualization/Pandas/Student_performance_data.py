import pandas as pd

data = {
    "Name": ["Alice","Bob","Charlie","David","Eva","Frank","Grace","Hannah"],
    "Department": ["CS", "ECE", "CS", "ME", "EE", "CS", "ECE", "EE"],
    "Marks": [85, 68, 92, 74, 88, 59, 78, 95],
    "Attendance": [90, 75, 82, 95, 78, 85, 92, 70],
}

df = pd.DataFrame(data)

print("--- First 5 Students ---")
print(df.head(5))

avg_marks = df["Marks"].mean()
print(f"\nAverage Marks: {avg_marks:.2f}")

print("\n--- Students Scoring > 75 ---")
print(df[df["Marks"] > 75])

print("\n--- Students with Attendance < 80% ---")
print(df[df["Attendance"] < 80])

print("\n--- Students Sorted by Marks ---")
print(df.sort_values(by="Marks", ascending=False))
