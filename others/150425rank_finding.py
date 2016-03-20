'''
divede and conquer
pointsSet is the set of the points
the rank of a point is finally saved as the 3rd element of the point represented by a list
'''

def rankFinding():
    if partitionSeq(pointsSet,n//2,n):
        mean=partitionSeq(pointsSet,n//2,n)
        rankFinding()
        for item in pointsSet and item>mean:
            for items in pointsSet and items<mean:
                if item[1]<items[1]:
                    rank+=1
                    item[2]=rank
    return pointsSet

def partitionSeq(theSeq,middle,last):
    pivot=theSeq[middle]
    left=middle+1
    right=last
    while left<=right:
        while left<right and theSeq[left]<pivot:
            left+=1
        while right>=left and theSeq[right]>=pivot:
            right-=1
        if left<right:

            temp=theSeq[left]
            theSeq[left]=theSeq[right]
            theSeq[right]=temp
    if right!=first:
        theSeq[first]=theSeq[right]
        theSeq[right]=pivot
    return right


'''
straightforward
'''

def rankFindingStr():
    pointsSetStr.sort()
    for item in pointsSetStr:
        rankStr=0
        for i in range(0,item):
            if pointsSetStr[i]<pointsSetStr[item]:
                rank+=1
    pointsSetStr[item][2]rank
    return pointsSetStr

    
