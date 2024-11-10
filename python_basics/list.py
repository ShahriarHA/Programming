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


