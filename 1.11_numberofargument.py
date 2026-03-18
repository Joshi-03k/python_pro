#create function which shell accept any number of arguments and total display of all the numbers given as argument


def find_total(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Total =", total)

find_total(40, 20, 30)
find_total(5,50,60,70,10)
