# Get first number 
num1_first= input("Enter the first number: ")
num1 = float(num1_first)

# Get the desired operation 
operation = input("Enter the operation (+, -, *, /): ")

# Get the second number
num2_sec = input("Enter the second number: ")
num2 = float(num2_sec)

# Perform the calculation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0: 
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please use +, -, *, or /.")