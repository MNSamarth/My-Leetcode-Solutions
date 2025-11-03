class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=1
        cmax=0
        if(len(s)==1 or len(s)==0):
            return len(s)
        while(left<len(s)-1 and right<len(s)):
            if s[right] in s[left:right]:
                left+=1
                l=(right-left)+1
                if(l>cmax):
                    cmax=l
            else:
                right+=1
        if((right-left)>cmax):
            cmax=right-left
        return cmax