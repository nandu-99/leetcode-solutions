class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        ans = 0 
        lenn = 0 
        for num in nums:
            if num>=minK and num<=maxK:
                lenn+=1
                ans+=lenn 
            else:
                lenn=0
        return ans