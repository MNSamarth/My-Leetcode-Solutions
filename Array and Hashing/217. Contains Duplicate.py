class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a={}
        for num in nums:
            if num in a:
                return True
            else:
                a[num]=1
        return False