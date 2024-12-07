# Dictionary items are ordered, changeable, and do not allow duplicates.

thisdict = {
    "name":"shahriar",
    "DOB":"26th of october 1999",
    "Address":"Golapgonj,sylhet,Bnagladesh"
}
print(thisdict)

# Dictionaries cannot have two items with the same key:
# Duplicate values will overwrite existing values:

print(len(thisdict))
print(type(thisdict))

# use the dict() constructor to make a dictionary.
newDict = dict(a=10,b=34,c=45,name="Jhon",age=20,country="Bnagladesh")
print(newDict)

# access the items of a dictionary by referring to its key name, inside square brackets:
print(newDict["a"])
print(newDict["name"])
# There is also a method called get() that will give you the same result:
print(newDict.get("country"))

# The keys() method will return a list of all the keys in the dictionary.
print(newDict.keys())

# assign new items to the dict
newDict["favColor"] = "red"
newDict["hairColor"] = "Black"
print(newDict.keys())

# The values() method will return a list of all the values in the dictionary.
print(newDict.values())

# The items() method will return each item in a dictionary, as tuples in a list.
print(newDict.items())

# Check if "name" is present in the dictionary:
if "name" in newDict:
    print("yes!")
else:
    print("no!")

# change the value of a specific item by referring to its key name:
newDict["name"] = "Daizi"
print(newDict["name"])

# The update() method will update the dictionary with the items from the given argument.
# he argument must be a dictionary, or an iterable object with key:value pairs.
newDict.update({"age":30})
print(newDict.get("age"))
print(newDict.values())

# The pop() method removes the item with the specified key name:
newDict.pop("favColor")
print(newDict)

# The popitem() method removes the last inserted item
# The del keyword removes the item with the specified key name:
# The clear() method empties the dictionary:








