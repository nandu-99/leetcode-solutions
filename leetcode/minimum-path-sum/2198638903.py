class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = {}
        def recur(i, j):
            if (i, j) in d:return d[(i, j)]
            if i==m-1 and j==n-1:return grid[i][j]
            if i>m-1 or j>n-1:return float('inf')
            down = recur(i+1, j)
            right = recur(i, j+1)
            d[(i, j)] = grid[i][j] + min(down, right)
            return d[(i, j)]
        return recur(0, 0)
