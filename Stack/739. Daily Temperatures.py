class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        l=len(temperatures)
        answer=[0]*l
        count=0
        for i in range(l):
            t=temperatures[i]
            if not stack:
                stack.append(i)
            else:
                if(t>temperatures[stack[-1]]):
                    while(stack and t>temperatures[stack[-1]]):
                        answer[stack[-1]]=i-stack[-1]
                        stack.pop()
                stack.append(i)
        return answer