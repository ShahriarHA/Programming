# A set is a collection which is unordered, unchangeable*, and unindexed.
a_set = {"apple","banana","cherry"}
print(a_set)
print(len(a_set))
print(type(a_set))

# The set() Constructor
set1 = set(("apple","banana","cherry",10,True))
print(set1)

# Set items are unordered, unchangeable, and do not allow duplicate values.

# The values True and 1 are considered the same value in sets, and are treated as duplicates:
set2 = {"apple", "banana", "cherry", True, 1, 2}
print(set2)
# The values False and 0 are considered the same value in sets, and are treated as duplicates:

# To add one item to a set use the add() method.
set2.add("orange")
print(set2)
up_set = {5,6,7}
set2.update(up_set)
print(set2)

# To remove an item in a set, use the remove(), or the discard() method.
set2.discard(5)
print(set2)

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The clear() method empties the set:
set2.clear()
print(set2)

# he del keyword will delete the set completely:
del set1
# print(set1)

set1 = {"a", "b", "c"}
set3 = {1, 2, 3}
set4 = set1.union(set3)
print(set4)
# You can use the | operator instead of the union() method, and you will get the same result.
set5 = {"John", "Elena"}
set6 = {"apple", "bananas", "cherry"}
set7 = set4|set5|set6
print(set7)








