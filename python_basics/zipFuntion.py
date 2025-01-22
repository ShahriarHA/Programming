a = [1,2,3,4]
b = ['a','v','d','c','f','t','h']

for item1,item2 in zip(a,b):
    # print(item1,item2)
    pass

# using itertools.zip_longest
# This function fills the shorter list with a specified value (default is None) to ensure that both lists can be traversed completely.
from itertools import zip_longest as zl
for i1,i2 in zl(a,b,fillvalue=None):
    # print(i1,i2)
    pass

for i,item in enumerate(a):
    # print(i,item)
    val1 = item
    val2 = b[i]
    print(val1,val2)




