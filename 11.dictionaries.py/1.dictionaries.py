# create dictionaries are key value pairs

# create empty dictionary
usernames = {
    'admin': 'admin',
    'user1': 'user1',
    'user2': 'user2',
    'user3': 'user3',
    'user4': 'user4'
}
print(usernames['admin'])

# add new item to dictionary
usernames['user5'] = 'user5'
print(usernames)

# access dictionary items
for user in usernames:
    print(user)
  
# remove item from dictionary
del usernames['user5']
print(usernames)

# update item in dictionary
usernames['user1'] = 'abbas'
print(usernames)

# get dictionary keys
print(usernames.keys())

# get dictionary values
print(usernames.values())

# get dictionary items
print(usernames.items())

# get dictionary length
print(len(usernames))

# get dictionary value by key
print(usernames.get('user1'))

# copy dictionary
usernames2 = usernames.copy()
print(usernames2)

# nested dictionary create
usernames3 = {
    'admin': {
        'username': 'admin',
        'password': 'admin'
    },
    'user1': {
        'username': 'user1',
        'password': 'user1'
    },
}

# clear dictionary
usernames.clear()
print(usernames)


