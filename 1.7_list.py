#Write a program to create a list and perform various operations on list using menu.

lst=[]

while True:
    print("\n====Menu====")
    print("1.Add element")
    print("2.Delete element")
    print("3.Display list")
    print("4.Sort list")
    print("5.Search element")
    print("6.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        item=int(input("Enter element to add:"))
        lst.append(item)
        print("Element added")

    elif choice==2:
        item=int(input("Enter element to delete:"))
        if item in lst:
            lst.remove(item)
            print("Element deleted")
        else:
            print("Element not found")

    elif choice==3:
        print("List elements:",lst)

    elif choice==4:
        lst.sort()
        print("Sorted list is:",lst)

    elif choice==5:
        item=int(input("Enter element to search:"))
        if item in lst:
            print("Element found in list")
        else:
            print("Element not found")

    elif choice==6:
        print("Exit from program")
        break

    else:
        print("Enter valid choice...")
        
    

