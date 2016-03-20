def functionN(n,total):
	if(n==1):
		return total
	return functionN(n-1,n*total)

functionN(10000000,1)

