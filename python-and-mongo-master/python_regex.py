import re

#Returns a Match Object
#A Match Object is an object containing information about the search and the result.
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)
print(x.endpos)

# Span returns a tuple containing the start-, and end positions of the match
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())

# string returns the string passed into the function
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.string)

# group() returns the part of the string where there was a match
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())

# Returns a List of Matches
str = "The rain in Spain"
x = re.findall("ai", str)
print("Result of Final All" + x.__str__())

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())

str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)
if x is None:
    print("No Match Found")

# Split the String at First Occurance
str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)

# Replace space with 9
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)

# Replace only first 2 occurances
str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)