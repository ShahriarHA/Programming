
import json 
x = '{ "name":"John", "age":30, "city":"New York"}' #json string

print("----converting json into python----")
x_p = json.loads(x)
print(x_p)
print(type(x_p))

print("----geting back to json format----")
x_j = json.dumps(x_p)
print(x_j)
print(type(x_j))

