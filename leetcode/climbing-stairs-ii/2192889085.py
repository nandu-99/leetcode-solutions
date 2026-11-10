class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        d = {}
        def recur(i):
            if i in d:return d[i]
            if i>=n:return 0
            ans = float('inf')
            for j in range(1, 4):
                if i + j <= n:
                    ans = min(ans, costs[i+j-1]+((j)**2)+recur(i+j))
            d[i] = ans
            return d[i]
        return recur(0)