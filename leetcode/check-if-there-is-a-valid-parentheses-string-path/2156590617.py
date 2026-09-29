class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0]==")" or grid[m-1][n-1]=="(" or ((m + n - 1) % 2 == 1): return False 
        d = {}
        def recur(i, j, balance):
            if i>=m or j>=n:return False
            if grid[i][j]=="(": balance+=1 
            else: balance-=1 
            if balance<0:return False 
            if i==m-1 and j==n-1: return balance==0 
            state = (i, j, balance)
            if state in d:return d[state]
            down = recur(i+1, j, balance)
            right = recur(i, j+1, balance)
            d[state] = down or right 
            return d[state]
        return recur(0, 0, 0)