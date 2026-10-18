import math
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        d = {}
        def recur(eggs, floors):
            if floors<=1 or eggs==1:
                return floors
            if (eggs, floors) in d:return d[(eggs, floors)]
            l, h = 1, floors
            ans = floors 
            while l<=h:
                m = (l+h)//2 
                break_case = recur(eggs-1, m-1)
                not_break = recur(eggs, floors-m)
                ans = min(ans, 1+max(break_case, not_break))
                if break_case<not_break:
                    l = m+1 
                else:
                    h = m-1 
            d[(eggs, floors)] = ans 
            return ans 
        return recur(k, n)