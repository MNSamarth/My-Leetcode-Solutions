# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        current=head
        while(current):
            stack.append(current.val)
            current=current.next
        rev=None
        if stack:
            prev=ListNode(stack.pop())
            head=prev
            while(stack):
                rev=ListNode(stack.pop())
                prev.next=rev
                prev=rev
        return head
