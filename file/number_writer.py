import json

numbers =[1,2,4,7,4,8,3]
filename = 'number.json'
with open(filename,'a') as f_obj:
	json.dump(numbers,f_obj)