# gathering User Inputs

number1 = input("Enter your number: ")
operation = input("Choose & type an operation: ")
number2 = input("Enter your second number: ")

# Data type conversion and Input validation
try:
    number1 = float(number1)
    number2 = float(number2)
except ValueError :
    print("Please enter a new number") 
    exit()

# Conditional Math Operations

if operation == "+":
    print(number1+number2)
elif operation == "-":
    print(number1-number2)
elif operation == "*":
    print(number1*number2)
elif operation == "/":
    try: 
        print(number1/number2)
    #Division by Zero Protection 
    except ZeroDivisionError:
        print("Numbers can not be divided by 0!")
else :
    print("Please choose a new operation")