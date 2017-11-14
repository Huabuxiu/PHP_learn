import sys

print('This command line argument are:')
for i in sys.argv:
	print(i)

print('\n\nThe PYTHONPATH is ',sys.path,'\n')