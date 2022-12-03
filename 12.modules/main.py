from lib.operations import *
from lib.userInput import userInput

num1 = userInput()
num2 = userInput()
result = sum(num1, num2)
print(result)

results = subtract(num1, num2)
print(results)
