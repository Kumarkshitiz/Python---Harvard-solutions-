string = input("Expression: ")

num1, operator,  num2  = string.split()
num1 = float(num1)
num2 = float(num2)
if operator == "+":
    expr = num1 + num2
    print(expr)
elif operator == "-":
    expr = num1 - num2
    print(expr)
elif operator == "*":
    expr = num1 * num2
    print(expr)
elif operator == "/" and (num2)!=0.0:
    expr = num1 / num2
    print(expr)
else:
    print("Wrong input")

