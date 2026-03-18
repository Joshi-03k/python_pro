#ut-2 basic exception handling pro-1

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")

except Exception as e:
    print("Some other error occurred:", e)

finally:
    print("Program execution completed, with or without error ")
