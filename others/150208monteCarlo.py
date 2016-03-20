import numpy as np
import random
count=0
n=1000000
for i in range(1,n):
    a1=random.random()
    x=a1*np.pi
    y=random.random()
    if y<np.sin(x):
        count+=1

area=np.pi*1*(float(count))/n
print area
