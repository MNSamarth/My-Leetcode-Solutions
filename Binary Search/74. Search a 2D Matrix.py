class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        l=r*c
        left=0
        right=l-1
        while(left<=right):
            m=int((left+right)//2)
            row=int(m//c)
            col=int(m%c)
            if target==matrix[row][col]:
                return True
            elif target<matrix[row][col]:
                right=m-1
            else:
                left=m+1
        return False