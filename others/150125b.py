import time
L=1
for i in range(1,24):
    L=L*i
print L
def selfCancel(a):
    while(a>=0):
        a-=1
def timer(func,*args):
    start=time.clock()
    func(*args)
    return time.clock()-start
print timer(selfCancel,L)
