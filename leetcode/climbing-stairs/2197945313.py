class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        def recur(i):
            if i in d:return d[i]
            if i==n:return 1 
            if i>n:return 0 
            d[i] = recur(i+1)+recur(i+2)
            return d[i]
        return recur(0)