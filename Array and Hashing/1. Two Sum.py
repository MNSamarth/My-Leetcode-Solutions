class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash={}
        for i in range (len(nums)):
            c=target-nums[i]
            if c in hash:
                return [nums.index(c),i]
            else:
                hash[nums[i]]='\0'