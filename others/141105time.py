"""
calculate the time consuming of certain function
"""
import time
def timer(func,*args):
    start=time.clock()
    for i in range(0,10000):
        func(*args)
    return time.clock()-start
def test1(x):
    x=1
    for i in range(1,100):
        for j  in range(1,100):
            x+=2
    return x
"""
test test1
"""
test2=test1(2)
test3=timer(test1,2)
print test2
print str(test3)+'s'
