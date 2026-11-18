class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def lcs(s, t):
            d = {}
            def recur(i, j):
                if (i, j) in d:return d[(i, j)]
                if i>=len(s) or j>=len(t):
                    return 0 
                if s[i]==t[j]: d[(i, j)] = 1+recur(i+1, j+1)
                else:
                    d[(i,j)] = max(recur(i+1, j), recur(i, j+1))
                return d[(i, j)]
            return recur(0, 0)
        return lcs(s, s[::-1])