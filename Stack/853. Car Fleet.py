class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined=list(zip(position,speed))
        combined.sort(reverse=True)
        position, speed= list(zip(*combined))
        position=list(position)
        speed=list(speed)
        stack=[]
        n=len(position)
        fleet=[0]*n
        # for i in range(n):
        #     position[i]+=speed[i]
        #     if not stack:
        #         stack.append(i)
        #         fleet[stack[-1]]=1
        #     else:
        #         if position[i]>=position[stack[-1]] and fleet[i]==0:
        #             if speed[i]>speed[stack[-1]]:
        #                 speed[i]=speed[stack[-1]]
        #             else:
        #                 speed[stack[-1]]=speed[i]
        #             fleet[i]==1
        #         else:
        #             stack.append(i)
        # return fleet+len(stack)
        for i in range(n):
            time=((target-position[i])/speed[i])
            if not stack:
                stack.append(time)
            else:
                if time>stack[-1]:
                    stack.append(time)
        return len(stack)




        