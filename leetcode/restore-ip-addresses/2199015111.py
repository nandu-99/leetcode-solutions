class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        def valid(temp):
            if len(temp)>3 or len(temp)==0:
                return False 
            if len(temp)>1 and temp[0]=='0':
                return False 
            if len(temp) and int(temp)>255:
                return False 
            return True
        
        def recur(ans, output, ind, s, dots):
            if dots==3:
                if valid(s[ind:]):
                    ans.append(output+s[ind:])
                return 
            for i in range(ind, min(ind+3, len(s))):
                if valid(s[ind:i+1]):
                    newo = output+s[ind:i+1]+"."
                    recur(ans, newo, i+1, s, dots+1)
        
        ans = []
        recur(ans, "", 0, s,  0)
        return ans
