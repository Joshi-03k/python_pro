#WAP to enter 10 number and find largest odd number

largest_odd=0
print("Enter 10 numbers:")

for i in range(10):
    num = int(input())
    if num % 2 !=0:

        if num>largest_odd:
            largest_odd=num

if largest_odd > 0:
    print("Largest odd number is:",largest_odd)
else:
    print("No numbers entered")

