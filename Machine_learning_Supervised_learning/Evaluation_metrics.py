from sklearn.metrics import (accuracy_score,confusion_matrix,f1_score,precision_score,recall_score,)

y_actual = [1, 1, 1, 0, 0, 0, 1, 0]
y_predicted = [1, 1, 0, 0, 0, 1, 1, 0]

accuracy = accuracy_score(y_actual, y_predicted)
precision = precision_score(y_actual, y_predicted)
recall = recall_score(y_actual, y_predicted)
f1 = f1_score(y_actual, y_predicted)

print("Evaluation Metrics ")
print(f"Accuracy : {accuracy:.2f} ({accuracy * 100:.0f}%)")
print(f"Precision: {precision:.2f} ({precision * 100:.0f}%)")
print(f"Recall   : {recall:.2f} ({recall * 100:.0f}%)")
print(f"F1-Score : {f1:.2f} ({f1 * 100:.0f}%)")

print("\nConfusion Matrix")
tn, fp, fn, tp = confusion_matrix(y_actual, y_predicted).ravel()
print(f"TP: {tp} | FP: {fp}")
print(f"FN: {fn} | TN: {tn}")
