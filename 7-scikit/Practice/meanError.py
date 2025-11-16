from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import pandas as pd
import numpy as np

df = pd.read_csv("7-scikit/Practice/student.csv")

x = df[["Hours"]]
y = df["Scores"]

# print("hours: ", hours)
# print("scores: ", scores)

model = LinearRegression()
model.fit(x, y)

predScores = model.predict(x)

print("predScores: ", predScores)

# Evalute
mae = mean_absolute_error(y, predScores)
print("mae: ", mae)
mse = mean_squared_error(y, predScores)
print("mse: ", mse)
rmse = np.sqrt(mse)
print("rmse: ", rmse)