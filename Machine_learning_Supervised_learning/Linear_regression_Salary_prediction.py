import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8],
    "Salary": [20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000],
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

exp_to_predict = pd.DataFrame([[5]], columns=["Experience"])
predicted_salary = model.predict(exp_to_predict)[0]

print(f"Predicted Salary for 5 years of experience: ${predicted_salary:,.2f}")
print(f"Model Equation: Salary = {model.intercept_:.0f} + {model.coef_[0]:.0f} * Experience")

plt.figure(figsize=(8, 5))
plt.scatter(df["Experience"],df["Salary"],color="blue",label="Actual Data",s=60,)
plt.plot(df["Experience"],model.predict(X),color="red",linewidth=2,label="Regression Line",)
plt.scatter([5],[predicted_salary],color="green",s=120,zorder=5,label=f"Prediction (5 yrs = ${predicted_salary:,.0f})",)

plt.title("Salary Prediction using Linear Regression", fontsize=14)
plt.xlabel("Years of Experience", fontsize=12)
plt.ylabel("Salary ($)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
