#python calculator

#Ask user to choose operator
operator = input("Enter an operator (+ - * /):")

#Ask user to enter numbers to operate with
#First typecast to change from String
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))


if  operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print (f"{operator} is not valid operator!")    