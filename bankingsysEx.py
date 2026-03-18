#ex..pro-6-banking sys 
balance = 0


def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount Deposited:", amount)
    print("Updated Balance:", balance)


def withdraw(amount):
    global balance
    if amount <= balance:
        balance = balance - amount
        print("Amount Withdrawn:", amount)
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance!")


def check_balance():
    print("Current Balance:", balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == 3:
        check_balance()

    elif choice == 4:
        print("Thank you for using the banking system!")
        break

    else:
        print("Invalid choice! Please try again.")
