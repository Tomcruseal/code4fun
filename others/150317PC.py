import operator
def combination(n,k):
    if(k==0):
        return 1
    else:
        return reduce(operator.mul,range(n-k+1,n+1))/reduce(operator.mul,range(1,k+1))
def permutation(n,k):
    if(k==0):
        return 1
    else:
        return reduce(operator.mul,range(n-k+1,n+1))
def factorial(n):
    return reduce(operator.mul,range(1,n+1))
print combination(5,0)
print permutation(5,0)
print factorial(5)
