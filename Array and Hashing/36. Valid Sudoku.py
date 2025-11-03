class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row={}
            col={}
            box={}
            for j in range(9):
                #computation for indices of box
                x=(j/3)+((i/3)*3)
                y=(j%3)+((i%3)*3)
                r=board[i][j]
                c=board[j][i]
                b=board[x][y]
                if r in row or c in col or b in box:
                    return False    
                if r!='.':
                    row[r]=1
                if c!='.':
                    col[c]=1
                if b!='.':
                    box[b]=1
        return True