#to create fibonaccie series up to enterd term

a=0
b=1

n=int(input("enter series:"))
print(a,b,sep="\n")

for i in range(10,n):
    c=a+b
    a=b
    b=c
    print("c")
