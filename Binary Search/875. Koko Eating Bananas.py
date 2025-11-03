class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        res=right
        if len(piles)==1:
            return ceil(piles[0]/h)
        while(left<=right):
            mid=int((left+right)/2)
            # print(mid)
            hours=0
            for p in piles:
                hours+=ceil(p/mid)
            # print(hours,mid)
            if hours<=h:
                res=min(res,mid)
                right=mid-1
            else:
                left=mid+1
        return res