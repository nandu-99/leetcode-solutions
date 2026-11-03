class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def calc(mid):
            bouq = 0 
            cdays = 0 
            for bloom in bloomDay:
                if bloom<=mid:
                    cdays+=1 
                    if cdays>=k:
                        bouq+=1 
                        cdays = 0 
                else:
                    cdays = 0 
            return bouq>=m 
        l  = 0 
        h = 1000000000
        ans = -1
        while l<=h:
            mid = (l+h)//2 
            if calc(mid):
                ans = mid 
                h = mid-1
            else:
                l = mid+1
        return ans
