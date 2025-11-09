from sklearn.linear_model import LinearRegression

x = [[1],[2],[3],[4],[5]]
y = [15, 25, 34, 44, 56]

model = LinearRegression()
model.fit(x, y)

hours = float(input("Enter how many hours you studies?"))

predictedMarks = model.predict([[hours]])

print(f"Based on your hours{hours}, you may get {predictedMarks} marks")
