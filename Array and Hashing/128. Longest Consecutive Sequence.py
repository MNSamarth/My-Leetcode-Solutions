class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n={}
        if not nums:
            return 0
        for i in nums:
            if i not in n:
                n[i]=1
        cmax=1
        for i in n:
            if i-1 not in n:
                j=i
                c=1
                while j+1 in n:
                    j+=1
                    c+=1
                if c>cmax:
                    cmax=c
        return cmax