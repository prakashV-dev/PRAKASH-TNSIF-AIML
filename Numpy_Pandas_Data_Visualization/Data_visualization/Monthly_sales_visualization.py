import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 13500, 18000, 21000, 19500],
}

df = pd.DataFrame(data)

print("--- Monthly Sales Data ---")
print(df)

plt.figure(figsize=(8, 5))
plt.plot(df["Month"],df["Sales"],marker="o",color="blue",linestyle="-",linewidth=2,label="Monthly Sales")

plt.title("Monthly Sales Trend (Jan - Jun)", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(df["Month"],df["Sales"],color="skyblue",edgecolor="navy",label="Sales ($)")

plt.title("Monthly Sales Comparison", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()
