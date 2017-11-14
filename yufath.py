def log(func):

	def wrapper(*args,**kwargs):
		print("%s is running"% func.__name__)
		return func(*args,**kwargs)
	return wrapper

@log
def bar():
	print('i am bar')

bar()