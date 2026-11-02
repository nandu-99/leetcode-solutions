class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def calc(m):
            s = 0 
            c = 1
            for i in weights:
                if s+i<=m:
                    s+=i 
                else:
                    c+=1 
                    s = i 
            return c<=days
        l = max(weights)
        h = sum(weights)
        while l<h:
            m = (l+h)//2 
            if calc(m):
                h = m 
            else:
                l = m+1 
        return l 
