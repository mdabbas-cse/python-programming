def sum(num1, num2):
    return num1 + num2

num1 = int(input("Enter first number: ")) # input from user and convert to int
num2 = int(input("Enter second number: "))
results = sum(num1, num2)

print(f"sum of {num1} and {num2} is {results}")
print("sum of {0} and {1} is {2}".format(num1, num2, results))
print("sum of {a} and {b} is {c}".format(a=num1, b=num2, c=results))