class Solution:
    def countValidSubstrings(self, s: str) -> int:
        n = len(s)
        last = -1
        ans = 0 
        for i in range(n):
            if i >= 2 and s[i-2:i+1] == "abc":
                last = i - 2
            ans += i - last
        return ans