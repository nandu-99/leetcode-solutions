class Solution:
    def minMoves(self, nums: list[int]) -> int:
        s = 0 
        mini = min(nums)
        for i in nums:
            s+=(i-mini)
        return s 