#ex-7(6,7,8,9,10,11,12)

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

# vii. Slicing operations
print("list1[-2]:", list1[-2])          # Second last element
print("list2[1:3]:", list2[1:3])        # Elements from index 1 to 2
print("list1[-1:-3]:", list1[-1:-3])    # Empty (wrong direction slicing)

# viii. Length of list2
print("Length of list2:", len(list2))

# ix. Maximum element in list1
# (Only numeric values can be compared, so we filter numbers)
numeric_list1 = [x for x in list1 if isinstance(x, (int, float))]
print("Maximum element in list1:", max(numeric_list1))

# x. Minimum element in list2
print("Minimum element in list2:", min(list2))

# xi. Append 100 to list2
list2.append(100)
print("After append 100:", list2)

# xii. Extend operation
list2.extend([200, 300])
print("After extend operation:", list2)
