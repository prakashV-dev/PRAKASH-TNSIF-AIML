import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = {
    "Age": [20, 22, 25, 28, 30, 32, 35, 38, 40, 45],
    "Income": [15000, 18000, 22000, 30000, 35000, 40000, 45000, 50000, 55000, 60000],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
}

df = pd.DataFrame(data)

X = df[["Age", "Income"]]
y = df["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train, y_train)

dec_tree = DecisionTreeClassifier(random_state=42)
dec_tree.fit(X_train, y_train)
new_customer = pd.DataFrame([[27, 28000]], columns=["Age", "Income"])

log_pred = log_reg.predict(new_customer)[0]
dt_pred = dec_tree.predict(new_customer)[0]

log_label = "Purchase (1)" if log_pred == 1 else "No Purchase (0)"
dt_label = "Purchase (1)" if dt_pred == 1 else "No Purchase (0)"

log_acc = accuracy_score(y_test, log_reg.predict(X_test))
dt_acc = accuracy_score(y_test, dec_tree.predict(X_test))

print("New Customer Prediction (Age = 27, Income = $28,000)")
print(f"Logistic Regression Prediction : {log_label}")
print(f"Decision Tree Prediction       : {dt_label}")

print("\n--- Model Accuracy Evaluation ---")
print(f"Logistic Regression Accuracy   : {log_acc * 100:.2f}%")
print(f"Decision Tree Accuracy         : {dt_acc * 100:.2f}%")
