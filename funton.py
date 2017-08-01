def pow(x,n=2):
	if n == 2:
		return x*x
	else:
		return x*pow(x,n-1)
	
