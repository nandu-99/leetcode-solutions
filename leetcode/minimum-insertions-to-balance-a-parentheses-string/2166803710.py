class Solution:
    def minInsertions(self, s: str) -> int:
        o = 0
        d = 0
        i = 0 
        while i < len(s):
            if s[i]=="(":
                o+=1 
                i+=1 
            else:
                if i+1<len(s) and s[i+1]==")":
                    i+=2 
                else:
                    d+=1 
                    i+=1 
                if o>0:o-=1 
                else:d+=1 
        return d +2*o