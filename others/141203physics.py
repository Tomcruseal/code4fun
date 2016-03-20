import numpy as np
n=2
number=float(float((np.cos(np.pi/(2*n)))))**(2*n)
#number1=float(number**(2*n))
while(number<0.6):
    n+=1
print n    
print number
