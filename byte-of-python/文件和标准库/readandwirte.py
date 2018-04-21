poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''

f = open('poem.txt','w')
f.write(poem)
f.close()

f = open('poem.txt')

print(f.readlines())
# while True:
# 	line = f.readline()
# 	if len(line)==0:
# 		break
# 	else:
# 		print(line)

f.close()