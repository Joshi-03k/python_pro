#WAP to perform arithmetic operation take two value and one operator

num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
op=input("Enter operator:")

if op=="+":
    print("Addition is:",num1+num2)

elif op=="-":
    print("Subtraction is:",num1-num2)

elif op=="*":
    print("Multiplication is:",num1*num2)

elif op=="/":
    print("Division is:",num1/num2)


else:
    print("Enter valid operator...")
