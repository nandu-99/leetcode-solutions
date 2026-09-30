class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        curr = 0 
        for ch in seq:
            if ch=="(":
                ans.append(curr%2)
                curr+=1 
            else:
                curr-=1 
                ans.append(curr%2)
        return ans