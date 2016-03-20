"""
this module is for quick-sort
"""
def partitionSeq(theSeq,first,last):
    pivot=theSeq[first]
    left=first+1
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



def recQuickSort(theSeq,first,last):
    if first>=last:
        return
    else:
       pivot=theSeq[first]
       pos=partitionSeq(theSeq,first,last)
       recQuickSort(theSeq,first,pos-1)
       recQuickSort(theSeq,pos+1,last)


def Quick(theSeq):
    n=len(theSeq)
    recQuickSort(theSeq,0,n-1)
    return theSeq
