class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        s=[1]*l
        j=l-2
        answer=[1]*l
        for i in range(1,l,1):
            answer[i]=answer[i-1]*nums[i-1]
            s[j]=s[j+1]*nums[j+1]
            j-=1
        for i in range(l):
            answer[i]*=s[i]
        return answer