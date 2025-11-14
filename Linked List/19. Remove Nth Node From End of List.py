# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        temp=head
        l=0
        while(temp!=None):
            l+=1
            temp=temp.next
        current=head
        prev=ListNode()
        print(l,n)
        if l==n:
            return current.next
        ind=0
        while(current!=None):
            if ind==l-n:
                prev.next=current.next
                break
            ind+=1
            prev=current
            current=current.next
        return head