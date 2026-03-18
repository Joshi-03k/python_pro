#ex7-13,14,15
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

# xiv. Difference between pop() and remove()

print("Original list2:", list2)

# pop() removes element by index and returns it
removed_item = list2.pop(2)
print("After pop(2):", list2)
print("Item removed using pop():", removed_item)

# remove() removes element by value
list2.remove(5)
print("After remove(5):", list2)

print("\nDifference:")
print("pop() → removes element using index and returns the removed value.")
print("remove() → removes element using value and does not return it.")

# xv. reverse() on list1
list1.reverse()
print("\nlist1 after reverse():", list1)

# xvi. Arrange elements in descending order in list2
list2.sort(reverse=True)
print("list2 in descending order:", list2)
