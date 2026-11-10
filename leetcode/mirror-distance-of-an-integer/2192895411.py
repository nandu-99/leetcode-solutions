class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n):
            s = 0 
            while n:
                s*=10 
                s+=n%10 
                n//=10 
            return s 
        return abs(n-reverse(n))