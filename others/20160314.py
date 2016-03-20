matrix=[]
counter=0
for xcounter in xrange(5):
	x=[]
	for ycounter in xrange(5):
		x.append('a')
		counter+=1
		matrix.append(x)

for counter in xrange(5):
	print "%c %c %c %c %c" % (matrix[counter][0], matrix[counter][1], matrix[counter][2], matrix[counter][3], matrix[counter][4])
	print "\n"	