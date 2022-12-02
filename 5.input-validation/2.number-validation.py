# number validation
userInput = input("Enter username: ")
if userInput.isdigit(): # check if input is a number
    print("number is not allowed")
if userInput.isalnum(): # check if input is a number or string
    print("number or string is not allowed {0}".format(userInput))
if userInput.isdecimal(): # check if input is a decimal
    print("decimal is not allowed")
if userInput.isnumeric(): # check if input is a numeric
    print("numeric is not allowed")
if userInput.isidentifier(): # check if input is a identifier
    print("identifier is not allowed")
if userInput.isprintable(): # check if input is a printable
    print("printable is not allowed")
if userInput.isascii(): # check if input is a ascii
    print("ascii is not allowed")

