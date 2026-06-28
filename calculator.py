print("===== SIMPLE CALCULATOR =====")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operator = input("Enter your operator (+, -, *, /): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operator == '+':
    print("Result =", num1 + num2)

elif operator == '-':
    print("Result =", num1 - num2)

elif operator == '*':
    print("Result =", num1 * num2)

elif operator == '/':
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid operator")