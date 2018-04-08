def pow(x,n=2):
	if n == 2:
		return x*x
	else:
		return x*pow(x,n-1)
a = pow(5,3)	
print(a)
