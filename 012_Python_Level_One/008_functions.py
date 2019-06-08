def my_func(param1='default'):
    """
    THIS IS THE DOCSTRING
    """
    print("my first python function! {}".format(param1))

print(my_func('awesome'))


def hello():
    return "hello"
print(hello())


def addNum(num1, num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, I need integers!"

print(type(addNum("2","3")))
print(type(addNum(2,3)))

print(addNum("2","3"))
print(addNum(2,3))

# FIlter
mylist = (1,2,3,4,5,6,7,8)

def even_bool(num):
    return num%2 == 0

print(even_bool(4))

evens = filter(even_bool,mylist)
print(list(evens))

evens = filter(lambda num: num%2==0,mylist)
print(list(evens))

# x = str("hello")
# print(x.lower())
# print(x.upper())

# tweet = "Go Sports! #Sports"
# result tweet.split('#')

print('x' in [1,2,3])
print('x' in [1,2,3, "x"])
