import os
#os For file delete

f = open("demofile.txt", "x")
f.write("This is x write")
f.close()

#This Mode Opens file for writing.
#If file does not exist, it creates a new file.
#If file exists it truncates the file.

f = open("demofile.txt", "w")
f.write("""OOPS ...This is a Demo File
Demo File is For Demo Purpose
I love python <3.""")
f.close()


try:
    f = open("demofile.txt", "rt")
finally:
    f.close()
#Here rt is default r=read and t=txt
#is same as f = open("demofile.txt")

f = open("demofile.txt", "rb")
print(f.read())
f.close()

#Read First 5 Chars
f = open("demofile.txt", "r")
print(f.read(5))
f.close()

#Read Line
f = open("demofile.txt", "r")
print(f.readline())
f.close()

#Read First 2 Lines
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()

#Read File using an iterator
f = open("demofile.txt", "r")
for x in f:
  print(x)
f.close()

#Append to thr end of file
f = open("demofile.txt", "a")
f.write("Now the file has one more line!")
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close()

#Delete File if exists
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")