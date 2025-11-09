from sklearn.neighbors import KNeighborsClassifier

x = [
    [125, 5],
    [190, 6],
    [225, 7],
    [280, 8],
    [346, 9],
    [476, 10],
]
y = [0, 0, 0, 1, 1, 1]

# 0 -  Apple, 1 - Orange
model = KNeighborsClassifier()
model.fit(x, y)

weight = float(input("Enter weight?"))
size = float(input("Enter size?"))

result = model.predict([[weight, size]])[0]
print(result)
if result == 1:
    print(f"it's likely a Orange")
else:
    print(f"it's likely a Apple")