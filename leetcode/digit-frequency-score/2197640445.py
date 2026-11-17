class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d = {}
        while n:
            di = n%10 
            d[di] = d.get(di, 0)+1 
            n//=10 
        # print(d)
        ans = 0 
        for i in d:
            ans+=i*d[i]
        return ans