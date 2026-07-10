import math

# Simple and clean math functions
def add(x, y): return x + y
def sub(x, y): return x - y
def mult(x, y): return x * y
def div(x, y): return x / y

print("=== Welcome to the Calculator ===")

while True:
    # 1. Get the first number or quit
    num1 = input("\nEnter a number (or type 'quit' to exit): ")
    if num1.lower() == "quit":
        print("Exiting program... Goodbye!")
        break
        
    try:
        num1 = float(num1)
    except ValueError:
        print("Error: Please enter a valid number!")
        continue  # Sends the user right back to the start of the loop
        
    # 2. Get the operator
    op = input("Choose an operator (+, -, *, /): ")
    if op not in ['+', '-', '*', '/']:
        print("Error: Invalid operator! Please try again.")
        continue  # Sends the user right back to the start of the loop
        
    # 3. Get the second number
    num2 = input("Enter the second number: ")
    try:
        num2 = float(num2)
    except ValueError:
        print("Error: Please enter a valid number!")
        continue
        
    res = None
    
    # 4. Perform the calculation
    if op == "+":
        res = add(num1, num2)
    elif op == "-":
        res = sub(num1, num2)
    elif op == "*":
        res = mult(num1, num2)
    elif op == "/":
        try:
            res = div(num1, num2)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
            continue

    # 5. Display the result and handle special math conditions
    if res is not None:
        print(f"Answer: {res}")
        
        if math.isinf(res):
            print("Ooops! The result is infinity!")
        elif math.isnan(res):
            print("Error: Undefined mathematical operation (NaN)!")
            
    # The loop naturally ends here and jumps straight back to the top 
