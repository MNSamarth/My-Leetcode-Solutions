class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max=-1
        while(left<right):
            if height[left]>=height[right]:
                area=(right-left)*height[right]
                right-=1
            else:
                area=(right-left)*height[left]
                left+=1
            if area>max:
                max=area
        return max