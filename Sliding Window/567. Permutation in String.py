class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1=len(s1)
        lens2=len(s2)
        left=0
        count=Counter(s1)
        temp={}
        print(count)
        l=0
        for right in range(lens2):
            if s2[right] in count:
                temp[s2[right]]=1+temp.get(s2[right],0)
                l+=1
            else:
                left=right+1
                temp={}
                l=0
            if l==lens1:
                if temp==count:
                    return True
                else:
                    if s2[left] in temp:
                        temp[s2[left]]-=1
                    l-=1
                    left+=1
        if temp==count:
            return True
        return False
                
        #     print(temp, s2[left], s2[right],l)
        #     if l==lens1:
        #         if temp==count:
        #             return True
        #         else:
        #             if s2[left] in temp:
        #                 temp[s2[left]]-=1
        #                 l-=1
        #             left+=1
        #     else:
        #         print(s2[right])
        #         if s2[right] in count:
        #             temp[s2[right]]=1+temp.get(s2[right],0)
        #             l+=1
        #         else:
        #             left=right
        #             temp={}
        #             l=0
        #     print(temp, left, right,l)
        # if temp==count:
        #     return True
        # return False