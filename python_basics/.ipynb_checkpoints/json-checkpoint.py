
import json 
x = '{ "name":"John", "age":30, "city":"New York"}' #json string

x_p = json.loads(x)
print(x_p)
