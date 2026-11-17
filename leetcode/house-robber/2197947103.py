class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        d = {}
        def recur(i):
            if i in d:return d[i]
            if i>=n:return 0 
            t = nums[i]+recur(i+2)
            nt = recur(i+1)
            d[i] = max(t, nt)
            return d[i]
        return recur(0)