# Making a simple calculator.


num1: float = float(input("Please insert num1:"))
num2: float = float(input("Please insert num2:"))

operation = input("Please choose an operation (* / - + %):")

# if operation == "*":
#     print(num1 * num2)


# if operation == "/":
#     print(num1 / num2)


# if operation == "-":
#     print(num1 - num2)


# if operation == "+":
#     print(num1 + num2)

# else:
#     print("Not valid operator !")


# Else if :

if operation == "*":
    print(num1 * num2)

elif operation == "/":
    print(num1 / num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "+":
    print(num1 + num2)

else:
    print("Not valid operator !")
