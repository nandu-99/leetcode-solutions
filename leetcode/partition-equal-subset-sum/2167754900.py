class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        tar = total // 2
        dp = [False] * (tar + 1)
        dp[0] = True
        for num in nums:
            for j in range(tar, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[tar]