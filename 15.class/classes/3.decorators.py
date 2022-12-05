def decorators(func):
    def wrapper():
        print("wrapper of decorator")
        func()

    return wrapper


# def func():
#     print("Hello")
# func = decorators(func)()

# for calling the function, we can use the @decorator syntax
@decorators
def func():
    print("Hello")


func()
