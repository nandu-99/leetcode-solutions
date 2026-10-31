class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        d = {}
        m, n = len(grid), len(grid[0])
        mod = 10**9+7

        def resolve(i, j, dir):
            while i<m and j<n and grid[i][j]==1:
                if dir==0:
                    i+=1 
                    dir = 1 
                else:
                    j+=1 
                    dir = 0 
            if i>=m or j>=n: return 0 
            return recur(i, j)

        def recur(i, j):
            if i>=m or j>=n:return 0 
            if i==m-1 and j==n-1:return 1 
            if (i, j) in d:return d[(i, j)]
            k = resolve(i, j+1, 0)
            k+=resolve(i+1, j, 1)

            
            d[(i, j)] = k%mod 
            return d[(i, j)]
        return recur(0, 0)