#Write a program to enter marks of 4 subjects and display result(result shall include total,percentage and grade)

m1=int(input("Enter python marks:"))
m2=int(input("Enter mobile programming mark:"))
m3=int(input("Enter computer network marks:"))
m4=int(input("Enter DAV marks:"))

total=m1+m2+m3+m4
per=total/4
print("Your total is:",total)
print("Your percentage is:",per,"%")

if per>=80 and per<=100:
    print("Grade is A")

elif per>=60 and per<80:
    print("Grade is B")

elif per>=40 and per<60:
    print("Grade is C")

else:
    print("You are fail...")
    
