Y=[10.6,1.6,8.8,2.6,-10,-0.1,-9.6,8.4,-0.5,\
   -7.6]
X=[0,1,2,3,4,5,6,7,8,9]
from scipy import stats
import numpy as np
import matplotlib.pyplot as pl
from pylab import *
Function1=stats.linregress(X,Y)
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
def Function2(t):
    return slope*t+intercept
#print Function1
t1=np.arange(0.0,20,0.01)
#print t1
#len_t1 = len(t1)/2  
#t1 = t1[0:len_t1]
#print len_t1
#print t1
pl.plot(t1,Function2(t1),'bo')
pl.show()


