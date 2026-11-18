class Solution:
    def numSquares(self, n: int) -> int:
        d = {}
        def recur(n):
            if n==0:return 0 
            if n in d:return d[n]
            if n<0: return float('inf')
            mini = n
            i = 1 
            while i*i<=n:
                mini = min(mini, recur(n-(i*i)))
                i+=1
            d[n] = mini+1
            return mini+1 
        return recur(n)
