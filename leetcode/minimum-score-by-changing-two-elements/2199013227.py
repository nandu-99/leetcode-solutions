class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        op1 = nums[n-3]-nums[0]
        op2 = nums[n-1]-nums[2]
        op3 = nums[n-2]-nums[1]
        return min(op1, op2, op3)
