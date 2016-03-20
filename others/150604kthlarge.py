def Select(L,l,r,k):
	if l>r:
		return -1
	if l==r:
		return L[l]
	i=partition(L,l,r)
	j=i-l+1
	
	if j==k:
		return L[i]
	elif j>k:
		
		return Select(L,l,i,k)
	else:
		
		return Select(L,i+1,r,k-j)

def partition(L,l,r):
	if l<r:
		i=l
		j=r
		x=L[i]
		while (i<j):
			while (i<j and L[j]>x):
				j=j-1
			if i<j:
				i+=1
				L[i]=L[j]
			while i<j and L[i]<x:
				i=i+1
			if i<j:
                                j-=1
				L[j]=L[i]

		L[i]=x
		return i
	
	return -1
L=[2,3,4,3,9,6,5,6,4,7,3,3,6,1]

def test(L):
	print "please input the k"
	k=input()
	if k>-1 and k<len(L):
		print "Hello World"
        	print Select(L,1,13,k)
	else:return False	

test(L)

