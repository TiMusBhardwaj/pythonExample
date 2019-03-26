#creating a function
def my_function():
  print("Hello from a function")
def my_function():
  print("Hello from a function second")
#calling a function
my_function()

#Parameterized Function
def my_function(fname):
  print("Hello ".join(fname) + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Default Value Example
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#return value example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Recursion
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


#Passing a function
def foo(f):
  print("Running parameter f().")
  f()

def bar():
  print("In bar().")

def myFunction():
  print("Inside My Function")

foo(bar)
foo(myFunction)

#Lambda
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytrippler = myfunc(3)

print(mydoubler(11))
print(mytrippler(11))


