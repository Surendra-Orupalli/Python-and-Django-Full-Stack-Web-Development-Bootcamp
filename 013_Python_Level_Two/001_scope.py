x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())

my_func()
print(x)


# LOCAL
lambda x: x**2

# Enclosing function locals
name = "This is global name!"

def greet():
    name = "Sammy"

    def hello():
        print("hello " + name)

    return hello()

print(greet())

print(name)

print(len(name))



x = 50

def func(x):
    print("x is: ", x)
    x = 1000
    print("Local x changed to: ", x)

print(func(x))
print(x)

# Calling a global variable
x = 50

def func():
    global x
    x = 1500

print("Before function call, x is: ", x)

func()

print("After function call, x is ", x)




# Using return statement rather than global
x = 50

def func():
    x = 1500
    return x

print("Before function call, x is: ", x)

x = func()

print("After function call, x is: ", x)
