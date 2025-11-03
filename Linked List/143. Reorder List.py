# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        start=head
        while(start):
            current=start
            if current.next==None:
                break
            while(current.next.next!=None):
                current=current.next
            temp=current.next
            current.next=None
            temp.next=start.next
            start.next=temp
            start=start.next.next