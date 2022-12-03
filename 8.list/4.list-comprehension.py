#create new usernames list
usernames = ['admin', 'user1', 'user2', 'user3', 'user4']
# compere another list with usernames list

newLists =  [x for x in usernames if "u" in x]
print(newLists)

# create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newNumbers = [x for x in numbers if x < 5]
print(newNumbers)

# for even numbers
evenNumbers = [x for x in numbers if x % 2 == 0]
print(evenNumbers)

# for odd numbers
oddNumbers = [x for x in numbers if x % 2 != 0]
print(oddNumbers)