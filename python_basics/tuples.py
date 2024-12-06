mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# tuple length
print(len(mytuple))
print(range(len(mytuple)))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("hello",)
print(type(thistuple))
thistuple1 = ("hello")
print(type(thistuple1))

# it is also possible to use the tuple() constructor to make a tuple.
contuple = tuple(("my","name","shahriar"))
print(type(contuple))

# You can access tuple items by referring to the index number, inside square brackets:
print(contuple[0])
print(contuple[-1])

# range of indexes
r_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(r_tuple[1:5])

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x_tuple = ("cherry", "orange", "kiwi")
print("x = ", x_tuple)
y_tuple = list(x_tuple)
print(type(y_tuple))
y_tuple.append(10)
y_tuple.append(20)
y_tuple.append("melon")
y_tuple.insert(2,"hello")
print(y_tuple)
x_tuple = tuple(y_tuple)
print(x_tuple,type(x_tuple))

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
f1,f2,f3 = fruits
print(f1,f2,f3)

new_fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
nf1,nf2,*nf3 = new_fruits
print(nf1,nf2,nf3)

# Loop Through a Tuple
for x in new_fruits:
    print(x)
for i in range(len(fruits)):
    print(fruits[i])

# Join two tuples
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1,2,3)
my_tuple1 = tuple1 + tuple2
print(my_tuple1)

# multiply tuple items
print(my_tuple1 * 2)

# tuple nesting
tu1 = (1,2,3,4)
tu2 = ("python",)*3 #repeating iteems
nest = (tu1,tu2)
print(nest)

# unpacking tuple
print(tuple("shahriar"))

# nesting tuple within list
tpl = ([1,2,3],)
print(type(tpl))
ltp = list(tpl)
print(ltp,type(ltp))
ltp.append([222,34])
print(ltp)

tpl = tuple(ltp)
print(tpl)



