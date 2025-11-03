class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        top=-1
        for t in tokens:
            if t in ['+','-','/','*']:
                y=stack.pop()
                x=stack.pop()
                if t=='+':
                    stack.append(x+y)
                elif t=='-':
                    stack.append(x-y)
                elif t=='/':
                    stack.append(int(x/y))
                else:
                    stack.append(x*y)
            else:
                stack.append(int(t))
        return stack[-1]