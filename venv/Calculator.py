import math

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

operation = str(input("Choose an operation: \n add \n subtract \n multiply \n divide \n power \n mod \n"))

if operation == "add":
    print("Addition: ", x+y)
elif operation == "subtract":
    print("Subtraction: ", x-y)
elif operation == "multiply":
    print("Multiplication: ", x * y)
elif operation == "divide":
    print("Division: ", x / y)
    try:
        y == 0
    except ZeroDivisionError:
        print("Can't divide by 0")
elif operation == "power":
    print("power: ", x ** y)
elif operation == "mod":
    print("Mod: ", x % y)
else:
    print("WRONG")

