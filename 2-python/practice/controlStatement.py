num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

skip = int(input("Enter a number to skip: "))

# num2 should be greater than num1 for this loop to work correctly
if num2 <= num1:
    print("Error: Second number must be greater than the first number.")
elif skip <= num1 or skip >= num2:
    print("Error: Skip number must be between the first and second number.")
else:
    for i in range(num1, num2, 1):
        if i == skip:
            continue
        print(i)# Simple calculator using conditional statements

# Loop from num1 to num2, skipping the 'skip' numbers