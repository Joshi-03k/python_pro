# 1. Write a Function to Perform Arithmetic Operations

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Div by 0"


operations = { "1": ("+", add), "2": ("-", subtract),"3": ("*", multiply),"4": ("/", divide)}

choice = input("1.Add, 2.Sub, 3.Mul, 4.Div: ")

if choice in operations:
    num1 = float(input("First: "))
    num2 = float(input("Second: "))
    
    symbol, func = operations[choice]
    print(f"{num1} {symbol} {num2} = {func(num1, num2)}")
else:
    print("Invalid choice.")
