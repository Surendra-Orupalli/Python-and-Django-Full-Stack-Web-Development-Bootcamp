print(1 >= 1)

print((1>2) and (2<3))

if 1<2:
    print("First Block")
    if 20<3:
        print("Second Block")

if 1==1:
    if 1>2:
        print("hello")
    elif 3==3:
        print("elif ran")
    else:
        print("last")


seq = [1,2,3,4,5,6]

for item in seq:
    print(item)

d = {"Sam":1, "Frank":2, "Dan":3}

for item in d:
    print(item + ":" + str(d[item]))

mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)

for (tup1, tup2) in mypairs:
    print(tup2)
    print(tup1)

i = 1

while i<5:
    print("i is: {}".format(i))
    i = i+1

print(range(5))
print(list(range(0,20,2)))

for item in range(10):
    print(item)

x = [1,2,3,4]
out = []

for num in x:
    out.append(num**2)
print(out)

result = [num**2 for num in x]
print(result)
