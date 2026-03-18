#fibonacci series
a = 0
b =1

n = int(input("Enter number : "))
print(a,b,sep="\n")

for i in range(3,n):
   c=a+b
   a=b
   b=c
   print(c)
