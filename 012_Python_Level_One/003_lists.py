# Lists

mylist = [1,2,3]
mylist = ['stringstuff', 1, 2, 3, 4, True, 'asdf', [1,2,3]]
print(mylist)
print(len(mylist))

mylist =['a', 'b', 'c', 'd', 'e']
print(mylist[0])
print(mylist[-1])

mylist[0] = 'NEW ITEM'
print(mylist)

mylist.append("NEW ITEM")
print(mylist)

mylist.append(["x", "Y", "Z"])
print(mylist)

mylist.extend(["K", "L", "M"])
print(mylist)

item = mylist.pop(0)
print(mylist)
print(item)

mylist.reverse()
print(mylist)

numlist = [4,6,1,7,43,2]
print(numlist.sort())


mylist = (1,2,['x', 'y', 'z'])
print(mylist[2][1])

matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix[0][0]

# LIST COMPREHENSION
first_col = [row[0] for row in matrix]
print(first_col)
