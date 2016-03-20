class stack :
    def __init__(self):
        self._theItems=list()

    def isEmpty(self):
        return len(self)==0
    def pop(self):
        assert not self.isEmpty(),"Can not pop from an empty stack"
        return self._theItems.pop()
    def peek(self):
        assert not self.isEmpty(),"Can not peek at an empty stack"
        return self._theItems[-1]
    def push(self,item):
        self._theItems.append(item)
    def __len__ ( self ):
        return len( self._theItems )    
"""myStack=stack()
while ((input())!=0):
    temp=input()
    myStack.push(temp)
while(not myStack.isEmpty()):
    value=myStack.pop()
    print value
"""

myStack = stack()
value = int(input())
while value >= 0 :
    myStack.push( value )
    value = int(input())
while not myStack.isEmpty() :
    value = myStack.pop()
    print( value )        
        
    
