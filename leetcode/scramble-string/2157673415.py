class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        d = {}
        def recur(a, b):
            if a==b: return True 
            if sorted(a)!=sorted(b):return False 
            if (a, b) in d:return d[(a, b)]
            n = len(a)
            for i in range(1, n):
                if recur(a[:i], b[:i]) and recur(a[i:], b[i:]):
                    d[(a, b)] = True 
                    return True 
                if recur(a[:i], b[n-i:]) and recur(a[i:], b[:n-i]):
                    d[(a, b)] = True 
                    return True 
            d[(a, b)] = False 
            return False 
        return recur(s1, s2)