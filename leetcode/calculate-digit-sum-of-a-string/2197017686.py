class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def convert(s):
            v = 0 
            for i in s:
                v+=int(i)
            return str(v)
        
        while len(s)>k:
            ns = ""
            for i in range(0, len(s), k):
                ns+=convert(s[i:i+k])
            s = ns 
        return s