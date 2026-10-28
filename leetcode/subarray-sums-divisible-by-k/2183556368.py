class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        ps = 0 
        d = {0:1}
        ans = 0 
        for i in range(len(nums)):
            ps+=nums[i]
            mod = ps%k 
            if mod in d:
                ans+=d[mod]
                d[mod]+=1 
            else:
                d[mod]=1 
        return ans 