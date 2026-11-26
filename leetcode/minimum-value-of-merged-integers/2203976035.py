class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans = []
        for i in range(0,len(nums), 2):
            k = str(nums[i])+str(nums[i+1])
            ans.append(int(k))
        return min(ans)