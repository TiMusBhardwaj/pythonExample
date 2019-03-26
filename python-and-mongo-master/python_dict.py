
#Dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = thisdict["model"]
y = thisdict.get("model")
if x==y:
    print("Same Result")
#Dictionary constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
thisdict["year"] = 2018
print(thisdict)

#keys
for x in thisdict:
  print(x)
#values
for x in thisdict:
  print(thisdict[x])
for x in thisdict.values():
  print(x)
# Key and value
for x, y in thisdict.items():
  print(x, y)

#Key Exists ??
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print(len(thisdict))
#Add an item
thisdict["color"] = "red"
print(thisdict)

#POP
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#DEL
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#Clear
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)