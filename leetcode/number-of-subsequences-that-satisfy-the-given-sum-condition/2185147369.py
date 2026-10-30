class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        l = 0 
        c = 0 
        r = len(nums)-1 
        mod = 10**9+7
        while l<=r:
            if nums[l]+nums[r]<=target:
                c+=pow(2, r-l, mod)
                c%=mod 
                l+=1
            else:
                r-=1
        return c
                