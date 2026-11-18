class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return 0
        d = {}
        def recur(i, j):
            if (i, j) in d:return d[(i, j)]
            if i>m-1 or j>n-1:return 0
            if grid[i][j]==1: return 0 
            if i==m-1 and j==n-1:return 1 
            one = recur(i+1, j)
            two = recur(i, j+1)
            d[(i, j)] = one+two 
            return d[(i, j)]
        return recur(0, 0)
