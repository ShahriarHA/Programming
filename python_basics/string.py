# strings are arrays in python
a = "hello"
print(a[1])

# looping through a string
for x in a:
    print(x)

print(len(a))

# check string
txt = "the best things in life are free!"
if "free" in txt :
    print("yes!")
else:
    print("No!")

# slice string
print("------string slicing-----")
print(txt[4:8])
print(txt[:15])
print(txt[16:])
print("--------negative indexing!------")
neg_txt = "negative indexing"
print(neg_txt[-8:])
print(neg_txt[-8:-3])


