#create set
usernames = {'admin', 'user1', 'user2', 'user', 'user4'}
# print set
print(usernames)

# add new item to set
usernames.add('user5')
print(usernames)

# access set items
for user in usernames:
    print(user)

# remove item from set
usernames.remove('user5')
print(usernames)

