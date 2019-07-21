print("Hello")

mylisthere = [1,2,3]
print(mylisthere)

try:
    f = open("006_simple.txt", 'r')
    f.write("Test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()

print("hello world")

try:
    f = open("006_simple.txt", 'r')
    f.write("Test write to simple text!")
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()

print("hello world")


try:
    f = open("006_simple.txt", 'r')
    f.write("Test write to simple text!")
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")
