class Solution:
    def minEatingSpeed(self, piles: list[int], k: int) -> int:
        def calc(m):
            s = 0 
            for i in piles:
                if i%m==0:
                    s+=i//m 
                else:
                    s+=(i//m)+1 
            return s<=k
        l = 1 
        h = max(piles)
        while l<h:
            m = (l+h)//2 
            if calc(m):
                h = m 
            else:
                l = m+1 
        return l 