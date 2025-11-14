class Solution:
    def climbStairs(self, n: int) -> int:
        tab=[0]*(n+1)
        tab[0]=0
        if n>=1:
            tab[1]=1
        if n>=2:
            tab[2]=2
        for i in range(3,n+1):
            tab[i]=tab[i-1]+tab[i-2]
        return tab[n]