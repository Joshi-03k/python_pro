# Banking System Using Functions

balance = 0

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited:", amount)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Amount Withdrawn:", amount)

def check_balance():
    print("Current Balance:", balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)

    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
