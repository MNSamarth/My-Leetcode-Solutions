class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        lmax=height[left]
        rmax=height[right]
        units=0
        while(left<right):
            if lmax<=rmax:
                left+=1
                if height[left]>lmax:
                    lmax=height[left]
                else:
                    units+=lmax-height[left]
            else:
                right-=1
                if height[right]>rmax:
                    rmax=height[right]
                else:
                    units+=rmax-height[right]
        return units