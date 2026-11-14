class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        maxi = float('inf')
        for i in range(len(nums)):
            s = 0 
            for j in range(i, min(i+r, len(nums))):
                s+=nums[j]
                if j-i+1>=l and 0<s<maxi:
                    maxi = s 
        return -1 if maxi==float('inf') else maxi