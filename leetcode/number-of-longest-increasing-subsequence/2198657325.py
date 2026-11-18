class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        d = [1]*n 
        l = [1]*n 
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if d[i]<d[j]+1:
                        d[i] = d[j]+1 
                        l[i] = l[j]
                    elif d[i]==d[j]+1:
                        l[i]+=l[j]
        maxi = max(d)
        ans = 0 
        for i in range(n):
            if d[i]==maxi:
                ans+=l[i]
        return ans
