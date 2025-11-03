class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)
        if len(nums)==1 and target==nums[0]:
            return 0
        while(left<right):
            if target==nums[left]:
                return left
            else:
                left=left+1
        return -1