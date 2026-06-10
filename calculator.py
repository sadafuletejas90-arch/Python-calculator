print("Simple Calculator - calculator.py:1")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result: - calculator.py:8", num1 + num2)

elif operator == "-":
    print("Result: - calculator.py:11", num1 - num2)

elif operator == "*":
    print("Result: - calculator.py:14", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result: - calculator.py:18", num1 / num2)
    else:
        print("Error: Division by zero! - calculator.py:20")

else:
    print("Invalid operator! - calculator.py:23")