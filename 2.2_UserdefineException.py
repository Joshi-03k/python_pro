#user define exception pro-2
    
class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("You are not eligible to vote.")

    else:
        print("You are eligible to vote.")

except AgeError as e:
    print("User Defined Exception Occurred:", e)

except ValueError:
    print("Invalid input! Please enter a number.");
    
