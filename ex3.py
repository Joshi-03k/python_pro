#sum of n natural numbers

sum=0
n=int(input("enter value of  n"))

for i in range(1,n+1):
    sum=sum+i**2
    print("sum of natural num is :",sum)
    
