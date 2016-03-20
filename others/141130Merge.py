def pythonMergeSort(theList):
    if len(theList)<=1:
        return theList
    else:
        midpoint=len(theList)//2
        left=pythonMergeSort(theList[ :midpoint])
        right=pythonMergeSort(theList[midpoint: ])
    newList=merOrderedLists(left,right)
    return newList

#def newSorted(List1,List2):
    #return
listA=[2,5,3,89,34,56,13,12]
print pythonMergeSort(listA)
