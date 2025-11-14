class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        tab=[0]*(n+1)
        tab[0]=nums[0]
        if n>1:
            tab[1]=max(nums[1],nums[0])
            for i in range(2,n):
                tab[i]=max(tab[i-1],tab[i-2]+nums[i])
            tab[n]=max(tab[n-1],tab[n-2])
            print(tab)
            return tab[n]
        else:
            return tab[0]