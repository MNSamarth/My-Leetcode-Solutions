class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        tab=[0]*(n+1)
        tab[0]=cost[0]
        tab[1]=cost[1]
        for i in range(2,n):
            tab[i]=min(tab[i-1]+cost[i],tab[i-2]+cost[i])
        tab[n]=min(tab[n-1],tab[n-2])
        return tab[n]