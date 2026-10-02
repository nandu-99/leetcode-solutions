class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def recur(s, open, close):
            if len(s)==2*n:
                ans.append(s)
                return 
            if open<n:
                recur(s+"(", open+1, close)
            if close<open:
                recur(s+")", open, close+1)
        recur("", 0, 0)
        return ans