#Function to Calculate Factorial (Using Recursion)

def factorial_normal(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

num = int(input("Enter a number: "))

print("Factorial using normal function:", factorial_normal(num))
print("Factorial using recursive function:", factorial_recursive(num))



