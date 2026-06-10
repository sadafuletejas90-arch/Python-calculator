# Simple Calculator Program

# Display the title
print("Simple Calculator")

# Take the first number from the user
num1 = float(input("Enter first number: "))

# Take the operator from the user
operator = input("Enter operator (+, -, *, /): ")

# Take the second number from the user
num2 = float(input("Enter second number: "))

# Check if the operator is addition
if operator == "+":
    print("Result:", num1 + num2)

# Check if the operator is subtraction
elif operator == "-":
    print("Result:", num1 - num2)

# Check if the operator is multiplication
elif operator == "*":
    print("Result:", num1 * num2)

# Check if the operator is division
elif operator == "/":
    # Make sure the second number is not zero
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero!")

# If the operator is invalid
else:
    print("Invalid operator!")
