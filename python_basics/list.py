# check if item exists
list1 = ["apple","cherry","kiwi","michel",10]
if "apple" and 10 in list1:
    print("YES!")

# making a list using list() constractor
con_list = list(("my","name","shahriar"))
print(con_list)
print(type(con_list))

# change a range of item values
list1[1:4] = ["banana",20,25]
print(list1)

# The insert() method inserts an item at the specified index
con_list.insert(2,"arif")
print(con_list)

# To add an item to the end of the list, use the append() method
con_list.append("hussain")
print(con_list)

# To append elements from another list to the current list, use the extend() method
list1.extend(con_list)
print(list1)

# note: The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# remove specified items from list
re_list = ["apple", "banana", "cherry","kiwi"]
re_list.remove("kiwi")
print(re_list)
# If there are more than one item with the specified value, the remove() method removes the first occurrence:
# remove specified items using pop()

re_list.pop(0)
print(re_list)
# If you do not specify the index, the pop() method removes the last item.

# The clear() method empties the list.
re_list.clear()
print(re_list)

# loop list-----
l_list = ["cherry","banana","kiwi"]
for x in l_list:
    print(x)
# loop through the index numbers
for i in range(len(l_list)):
    print(l_list[i])

print("looping through list comprehension!")
[print(x) for x in l_list]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_f_list = []
for x in fruits:
    if "a" in x:
        new_f_list.append(x)

print(new_f_list)

# using loop comprehension
new_f_list.clear()
new_f_list = [x for x in fruits if "a" in x]
print(new_f_list)



