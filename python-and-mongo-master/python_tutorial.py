"""This is a
multiline docstring."""
print("Hello")
if 5 > 2:
  print("Five is greater than two!")

x = 5
y = "John"
print(x)
print(y)

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(x)
print(y)
print(z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(x)
print(y)
print(z)
print(w)

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print(x)
print(y)
print(z)


a = 33
b = 200
c = 800
if b > a:
    print("b is greater than a")
if a > b and c > a:
  print("Both conditions are True")


a = "Hello, World!"
print(a[1])

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello, World!"
print(len(a))
#x = input("Enter NAME")
#print("Hello, ", x)


print(6//3.0)

print(7/3.0)

print(~3)

##LIST
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist[1]="Tomato"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Index greater than present size will append the item.
thislist = ["apple", "banana", "cherry"]
thislist.insert(6, "orange")
#thislist[4]="pom" index out of bound
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry","apple"]
print(thislist.reverse())
print(thislist)
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  print("Index of apple in list : {}".format(thislist.index("apple")))
  print("Count of apple in list : {}".format(thislist.count("apple")))

#Tuple
#Its Just like list Just immutable
thistuple = tuple(("apple", "banana", "cherry","apple")) # note the double round-brackets
print(thistuple)

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits list")
  print("Index of apple in tuple : {}".format(thistuple.index("apple")))
  print("Count of apple in tuple : {}".format(thistuple.count("apple")))

