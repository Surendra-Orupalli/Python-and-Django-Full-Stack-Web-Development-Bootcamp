#STRINGS

#Basics
print("I'm a dog")

mystring = "abcdefg"
print(mystring[-4])

print(mystring[:3])
print(mystring[2:5])
print(mystring[:])
print(mystring[::])
print(mystring[::1])
print(mystring[::2])

X = mystring.upper()
print(X)

Y = mystring.capitalize()
print(Y)

mystring = "Hello World"

Z = mystring.split()
print(Z)

A = mystring.split('e')
print(A)

B = "Insert another string here: {}".format("INSERT ME")
print(B)

C = "Item One: {} Item Two: {}".format("dog", "cat")
print(C)

C = "Item One: {x} Item Two: {y}".format(x="dog", y="cat")
print(C)

D = "Item One: {y} Item Two: {x}".format(x="dog", y="cat")
print(D)

E = "Item One: {y} Item Two: {y}".format(x="dog", y="cat")
print(E)

# mystring[0] = 'X' --> strings are immutable
