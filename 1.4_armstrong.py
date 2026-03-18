#WAP to enter 10 numbers and display all armstrong numbers from those numbers

for i in range(1,11):
    num=int(input(f"Enter number {i}:"))


    digits=str(num)
    n=len(digits)
    total=sum(int(digit) ** n for digit in digits)

    if num==total:
        print(num, "is armstrong number")

    else:
        print(num, "is not armstrong number")

