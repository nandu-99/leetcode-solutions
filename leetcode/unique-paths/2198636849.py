class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = {}
        def recur(i, j):
            if (i, j) in d:return d[(i, j)]
            if i==m-1 and j==n-1: return 1 
            if i>m-1 or j>n-1: return 0 
            one = recur(i+1, j)
            two = recur(i, j+1)
            d[(i, j)] = one+two 
            return d[(i, j)]
        return recur(0, 0)