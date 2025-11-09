from sklearn.linear_model import LogisticRegression

x = [[1],[2],[3],[4],[5]]
y = [0, 0, 0, 1, 1]

model = LogisticRegression()
model.fit(x, y)

hours = float(input("Enter how many hours you studies?"))

result = model.predict([[hours]])[0]

if result == 1:
    print(f"Based on your hours{hours}, you are likely Pass")
else:
    print(f"Based on your hours{hours}, you are likely Fail")

