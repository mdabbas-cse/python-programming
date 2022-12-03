# numbers = input("Enter a list of numbers: ")
# numbers = list(numbers)
# print(numbers)

myList = [1, 2, 3, 4, 5]
# append a new item to the list
myList.append(6)
print(myList)

# insert a new item at a specific index
myList.insert(0, 0)
print(myList)

# remove an item from the list
myList.remove(2)
print(myList)

# remove an item from the list at a specific index
myList.pop(0)
print(myList)

# extend the list with another list
myList.extend([7, 2, 8, 9])
print(myList)

# remove all items from the list
myList.clear()
print(myList)