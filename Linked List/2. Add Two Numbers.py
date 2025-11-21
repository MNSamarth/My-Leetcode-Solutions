class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=0
        num2=0
        i=1
        while l1 or l2:
            if l1:
                num1=num1+l1.val*(i)
                l1=l1.next
            if l2:
                num2=num2+l2.val*(i)
                l2=l2.next
            i=i*10
        sum=num1+num2
        newNode=ListNode()
        current=newNode
        while(sum):
            current.val=sum%10
            sum=sum//10
            if sum > 0:
                current.next = ListNode()
                current = current.next
        return newNode