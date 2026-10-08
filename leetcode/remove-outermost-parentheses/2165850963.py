class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        d = 0 
        for i in s:
            if i=="(":
                d+=1 
                if d>1:
                    ans.append(i)
            elif i==")":
                d-=1 
                if d>0:
                    ans.append(i)
        return "".join(ans)