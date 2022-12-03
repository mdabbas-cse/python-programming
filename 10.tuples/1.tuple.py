#create tuple
usernames = ('admin', 'user1', 'user2', 'user3', 'user4')
# print tuple
print(usernames)
# access tuple items
for user in usernames:
    print(user)
# create new tuple
usernames2 = ('user5', 'user6', 'user7', 'user8', 'user9')
# join two tuple
usernames3 = usernames + usernames2
print(usernames3)
print(usernames3[0])

# unpack tuple items to variables
user1, user2, user3, user4, user5 = usernames
print(user1)
print(user2)
