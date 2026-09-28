class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        base = 0
        d = {}

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                base += 1
            else:
                x = nums[i - 1]
                y = nums[i]

                key = tuple(sorted((x, y)))
                d[key] = d.get(key, 0) + 1

        return base + (max(d.values()) if d else 0)