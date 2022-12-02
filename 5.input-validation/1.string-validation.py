# validation with default python types
userInput = input("Enter username: ")

if userInput.isalnum(): # check if input is a number or string
    print("number or string is not allowed {0}".format(userInput))
if userInput.isalpha(): # check if input is a string
    print("string is not allowed")
if userInput.islower(): # check if input is a lower case
    print("lower case is not allowed")
if userInput.isupper(): # check if input is a upper case
    print("upper case is not allowed")
if userInput.isspace(): # check if input is a space
    print("space is not allowed")
if userInput.istitle(): # check if input is a title
    print("title is not allowed")