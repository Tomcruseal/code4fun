class ListNode:                        #Node
    def __init__(self,data):
        self.data=data
        self.next=None
    
L1=ListNode(2)    
L2=ListNode(3)
L3=ListNode(4)
L1.next=L2
L2.next=L3
print L1.data,L1.next.data,L1.next.next.data
def tranverse(head):                   #tranverse the linked list
        curNode=head
        while curNode is not None:
            print curNode.data
            curNode=curNode.next
tranverse(L1)            

def unorderedSearch(head,target):      #search a data
    curNode=head
    while curNode is not None and curNode.data!=target:
        curNode=curNode.next
    return curNode is not None    
    
print unorderedSearch(L1,4)
print unorderedSearch(L1,998)
