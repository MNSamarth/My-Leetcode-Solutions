# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1=list1
        current2=list2
        head=ListNode()
        if not current1:
            return list2
        if not current2:
            return list1
        if current1.val<current2.val:
            head.val=current1.val
            current1=current1.next
        else:
            head.val=current2.val
            current2=current2.next
        prev=head
        while(current1 and current2):
            temp=ListNode()
            if current1.val<current2.val:
                temp.val=current1.val
                current1=current1.next
            else:
                temp.val=current2.val
                current2=current2.next
            prev.next=temp
            prev=temp
        while(current1):
            temp=ListNode()
            temp.val=current1.val
            current1=current1.next
            prev.next=temp
            prev=temp
        while(current2):
            temp=ListNode()
            temp.val=current2.val
            current2=current2.next
            prev.next=temp
            prev=temp
        return head
        