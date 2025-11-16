from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("7-scikit/Practice/student-scores.csv")

x = df[["weekly_self_study_hours"]]
y = df["math_score"]

# print("hours: ", hours)
# print("scores: ", scores)

model = LinearRegression()
model.fit(x, y)

predScores = model.predict(x)

print("predScores: ", predScores)

# Evalute
mae = mean_absolute_error(y, predScores)
print("mae: ", round(mae, 2))
mse = mean_squared_error(y, predScores)
print("mse: ", round(mse, 2))
rmse = np.sqrt(mse)
print("rmse: ", round(rmse, 2))

r2 = r2_score(y, predScores)
print("r2: ", round(r2, 2))

plt.figure(figsize=(10, 6))
plt.hist(y, bins=30, color="skyblue")
plt.title("Distribution of Math Score")
plt.xlabel("Math Score")
plt.ylabel("Number of Studenet")
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(x, y, label="Math Score")
plt.plot(x, predScores, color="Red")
plt.title("Distribution of Math Score")
plt.xlabel("Math Score")
plt.ylabel("Number of Studenet")
plt.grid(True)
plt.show()
