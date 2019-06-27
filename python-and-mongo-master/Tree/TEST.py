def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :  
args = ("Geeks", "for", "Geeks")
myFun(*args)


print(len("1"[1:]),"-------")