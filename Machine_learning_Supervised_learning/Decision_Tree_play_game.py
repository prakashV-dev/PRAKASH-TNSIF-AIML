import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

data = {
    "Weather": ["Sunny","Sunny","Rainy","Rainy","Cloudy","Cloudy","Sunny","Rainy",],
    "Temperature": ["Hot", "Cool", "Cool", "Hot", "Hot", "Cool", "Hot", "Cool"],
    "Play": [0, 1, 1, 0, 1, 1, 0, 1],
}

df = pd.DataFrame(data)

X = pd.get_dummies(df[["Weather", "Temperature"]], drop_first=False)
y = df["Play"]

model = DecisionTreeClassifier(criterion="entropy", random_state=42)
model.fit(X, y)

def predict_play(weather, temperature):
    input_data = pd.DataFrame(0, index=[0], columns=X.columns)
    weather_col = f"Weather_{weather}"
    temp_col = f"Temperature_{temperature}"
    if weather_col in input_data.columns:
        input_data[weather_col] = 1
    if temp_col in input_data.columns:
        input_data[temp_col] = 1
    prediction = model.predict(input_data)[0]
    result = "Yes (1)" if prediction == 1 else "No (0)"
    print(f"Input: Weather = {weather}, Temperature = {temperature}")
    print(f"Prediction (Play Game?): {result}\n")
    return prediction

print("Predictions")
predict_play("Sunny", "Cool")
predict_play("Rainy", "Hot")
predict_play("Cloudy", "Hot")

plt.figure(figsize=(10, 6))
plot_tree(model,feature_names=X.columns,class_names=["No (0)", "Yes (1)"],filled=True,rounded=True,fontsize=10,)
plt.title("Decision Tree for Playing Game", fontsize=14)
plt.tight_layout()
plt.show()
