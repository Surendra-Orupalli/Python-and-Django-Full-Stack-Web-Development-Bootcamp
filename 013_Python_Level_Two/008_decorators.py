# Straight forward case
def func():
    return 1

print(func())


# Global variable
s = "GLOBAL VARIABLE"
def func(s):
    print(s)

func(s)

# Local variable
s = "GLOBAL VARIABLE"
def func():
    s = 50
    print(s)

func()


# Global and Local variable
s = "GLOBAL VARIABLE"
def func():
    global s
    s = 50
    print(s)

func()


# Calling locals
s = "GLOBAL VARIABLE"
def func():
    mylocal = 10
    print(locals())
    print(globals())

func()


# Calling functions
def hello(name="Jose"):
    return "hello " + name

print(hello())

nmynewgreet = hello
print(nmynewgreet())


# Functions within Functions
def hello(name="jose"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")
    def greet():
        return "THIS STRING IS INSIDE GREET()"
    def welcome():
        return "THIS STRING IS INSIDE WELCOME!"
    print(greet())
    print(welcome())
    print("End of hello()")

hello()


# Returning Functions
def hello(name="jose"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")
    def greet():
        return "THIS STRING IS INSIDE GREET()"
    def welcome():
        return "THIS STRING IS INSIDE WELCOME!"

    if name == "jose":
        return greet
    else:
        return welcome

x = hello()
print(x())


# Function as an argument
def hello():
    return "Hi JOSE!"

def other(func):
    print("HELLO")
    print(func)

other(hello)


# Creating a decorator
def new_decorator(func):
    def wrap_func():
        print("CODE HERE BEFORE EXECUTING A FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")

# func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()
