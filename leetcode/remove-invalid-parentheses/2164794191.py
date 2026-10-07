class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isvalid(s):
            bal = 0 
            for i in s:
                if i=="(":
                    bal+=1 
                elif i==")":
                    bal-=1 
                    if bal<0:return False 
            return bal==0 
        
        q = deque([s])
        vis = {s}
        ans = []
        found = False
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if isvalid(curr):
                    ans.append(curr)
                    found = True 
                if found:continue 
                for i in range(len(curr)):
                    if curr[i] not in "()":continue 
                    nexs = curr[:i] + curr[i+1:]
                    if nexs not in vis:
                        vis.add(nexs)
                        q.append(nexs)
            if found:break 
        return ans

