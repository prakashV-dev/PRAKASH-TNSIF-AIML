import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

data = {
    "Age": [20, 22, 25, 28, 30, 35, 40, 45],
    "Income": [15000, 18000, 25000, 30000, 35000, 40000, 50000, 60000],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1],
}

df = pd.DataFrame(data)

X = df[["Age", "Income"]]
y = df["Purchased"]

model = LogisticRegression()
model.fit(X, y)

def predict_purchase(age, income):
    new_data = pd.DataFrame([[age, income]], columns=["Age", "Income"])
    prediction = model.predict(new_data)[0]
    probabilities = model.predict_proba(new_data)[0]

    result = "Yes" if prediction == 1 else "No"
    print(f"Input: Age = {age}, Income = ${income:,}")
    print(f"Prediction: {result} (Purchased = {prediction})")
    print(f"Probabilities -> No (0): {probabilities[0]:.2%}, Yes (1): {probabilities[1]:.2%}\n")
    return prediction

predict_purchase(24, 22000) # prediction1

predict_purchase(32, 38000) # prediction2

plt.figure(figsize=(8, 5))

for status, color, label in [(0, "red", "No (0)"), (1, "green", "Yes (1)")]:
    subset = df[df["Purchased"] == status]
    plt.scatter(subset["Age"],subset["Income"],color=color,label=f"Purchased: {label}",s=80,edgecolors="black",)
  
plt.scatter([24],[22000],color="blue",marker="*",s=250,zorder=5,label="Test Prediction (Age 24, $22k) -> No",)

plt.title("Logistic Regression — Product Purchase", fontsize=14)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Income ($)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
