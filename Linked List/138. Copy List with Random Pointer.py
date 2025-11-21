class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        temp=head
        ind={}
        while(temp!=None):
            ind[temp]=Node(temp.val)
            temp=temp.next
        copy=ind[head]
        current=copy
        while(head!=None):
            n=head.next
            r=head.random
            if r is not None:
                current.random=ind[r]
            else:
                current.random=None
            if n is not None:
                current.next=ind[n]
            else:
                current.next=None
            head=head.next
            current=current.next
        return copy