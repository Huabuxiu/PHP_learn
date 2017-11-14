import json
filename = 'number.json' 
with open(filename) as file_Obj:
	numbers = json.load(file_Obj)
print(numbers)