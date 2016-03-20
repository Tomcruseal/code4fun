import sys,time
reps=10000
repsList=list(range(reps))

def forLoop():
    res=[]
    for x in repsList:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x)for x in repsList]

def mapCall():
    return map(abs,repsList)

def genFunc():
    def gen():
        for x in repsList:
            yield abs(x)
    return list(gen())

def genExpr():
    return list(abs(x) for x in repsList)

def timer(func,*args):
    start=time.clock()
    for i in range(1000):
        func(*args)
    return time.clock()-start

print sys.version
print timer(forLoop),timer(listComp),\
      timer(mapCall),timer(genFunc),\
      timer(genExpr)


