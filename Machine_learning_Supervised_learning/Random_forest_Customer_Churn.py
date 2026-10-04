import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

data = {
    "Age": [22, 25, 30, 35, 40, 28, 45, 32],
    "Tenure": [2, 5, 1, 8, 10, 3, 12, 2],
    "Monthly Bill": [500, 600, 800, 550, 500, 900, 650, 850],
    "Churn": [1, 0, 1, 0, 0, 1, 0, 1],
}

df = pd.DataFrame(data)

X = df[["Age", "Tenure", "Monthly Bill"]]
y = df["Churn"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

def predict_churn(age, tenure, monthly_bill):
    customer = pd.DataFrame(
        [[age, tenure, monthly_bill]],
        columns=["Age", "Tenure", "Monthly Bill"],
    )
    prediction = model.predict(customer)[0]
    probabilities = model.predict_proba(customer)[0]
    status = "Leave (1)" if prediction == 1 else "Stay (0)"
    print(f"Customer Input -> Age: {age}, Tenure: {tenure} yrs, Bill: ${monthly_bill}")
    print(f"Predicted Churn: {status}")
    print(f"Confidence -> Stay (0): {probabilities[0]:.2%}, Leave (1): {probabilities[1]:.2%}\n")
    return prediction

print("Customer Predictions")
predict_churn(age=29, tenure=2, monthly_bill=820)
predict_churn(age=38, tenure=9, monthly_bill=520)
feature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=True)

plt.figure(figsize=(8, 4))
feature_importances.plot(kind="barh", color="teal", edgecolor="black")
plt.title("Random Forest — Feature Importances", fontsize=14)
plt.xlabel("Importance Score", fontsize=12)
plt.ylabel("Feature", fontsize=12)
plt.tight_layout()
plt.show()
