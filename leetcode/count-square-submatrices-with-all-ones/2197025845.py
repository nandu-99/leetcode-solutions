class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        d = {}
        def recur(i, j):
            if i<0 or j<0:return 0 
            if (i, j) in d:return d[(i, j)]
            if matrix[i][j]==0:return 0 
            if i==0 and j==0: return 1 
            
            d[(i, j)] = 1+min(recur(i-1, j), recur(i, j-1), recur(i-1, j-1))
            return d[(i, j)]
        m, n = len(matrix), len(matrix[0])
        ans = 0 
        for i in range(m):
            for j in range(n):
                ans+=recur(i, j)
        return ans