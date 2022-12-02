import pyinputplus as pyip

# 1. inputStr() - accepts only strings
# 2. inputNum() - accepts only numbers
# 3. inputChoice() - accepts only choices
# 4. inputMenu() - accepts only menu choices
# 5. inputDatetime() - accepts only date and time
# 6. inputYesNo() - accepts only yes or no
# 7. inputBool() - accepts only True or False
# 8. inputEmail() - accepts only email
# 9. inputFilepath() - accepts only file path
# 10. inputPassword() - accepts only password

name = pyip.inputStr(prompt='Enter your name: ')

print('Hello ' + name)