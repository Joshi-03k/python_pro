'''create 4 lambda functions which shall accept 2 numbers and 1 arithmetic operator . as per arithmetic operator related lambda func shall be invoked      '''

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Cannot divide by zero"


def calculate(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        return div(a, b)
    else:
        return "Invalid operator"


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")


result = calculate(num1, num2, operator)
print("Result:", result)
