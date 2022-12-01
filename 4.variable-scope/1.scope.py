#global variable
x = 10

def myFunc():
    # global x
    # x = 20
    print(x) # call global variable

myFunc()

# local variable
def myFunc2():
    x = 20
    print(x) # call local variable

myFunc2()