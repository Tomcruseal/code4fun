def ackermann(m,n):
	if m==0:
		return n+1
	elif m>0 and n==0:
		return ackermann(m-1,1)
	else:
		return ackermann(m-1,ackermann(m,n-1))

print "when m=3,n=3"
print ackermann(3,3)
