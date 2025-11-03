class Solution(object):

    def __init__(self):
        self.stack=[]
        self.top=-1

    def push(self,val):
        self.stack.append(val)
        self.top+=1

    def pop(self):
        self.top-=1
        return self.stack.pop()

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open={'(':')','{':'}','[':']'}
        for i in s:
            if i in open:
                self.push(i)
            else:
                if self.top==-1:
                    return False
                x=self.stack[-1]
                if open[x]==i:
                    self.pop()
                    continue
                else:
                    return False
        if self.top==-1:
            return True
        else:
            return False