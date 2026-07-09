# we should get user's numbers

number1 = input()
operation = input()
number2 = input()

number1 = float(number1)
number2 = float(number2)

if operation == "+":
    print(number1+number2)
elif operation == "-":
    print(number1-number2)
elif operation == "*":
    print(number1*number2)
else :
    print(number1/number2)    


