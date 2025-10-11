num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Enter operation (+, -, *, /): ")

if choice == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose from +, -, *, /.")# Simple calculator using conditional statements

