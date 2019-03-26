#https://www.8bitavenue.com/difference-between-del-remove-and-pop-in-python/
# (1) Remove an item with index
A = [1, 2, 4, 3, 4]
A.remove(4)
# This will print [1, 2, 3, 4]
print("Example 1 : A = {}".format(A))

# (2) Delete an item with index
A = [1, 2, 4, 3, 4]
del A[2]
# This will print [1, 2, 3, 4]
print("Example 2 : A = {}".format(A))

# (3) Delete all items
A = [1, 2, 4, 3, 4]
del A[:]
# This will print []
print("Example 3 : A = {}".format(A))

# (4) Delete a slice 2, 4
A = [1, 2, 4, 3, 4]
del A[1:3]
# This will print [1, 3, 4]
print("Example 4 : A = {}".format(A))

# (5) pop: remove and get the last item
A = [1, 2, 4, 3, 4]
x = A.pop()
# This will print [1, 2, 4, 3]
print("Example 5 : A = {}".format(A))
# This will print 4
print("Example 5 : x = {}".format(x))

# (6) pop with index: remove and get the second item
A = [1, 2, 4, 3, 4]
x = A.pop(1)
# This will print [1, 4, 3, 4]
print("Example 6 : A = {}".format(A))
# This will print 2
print("Example 6 : x = {}".format(x))