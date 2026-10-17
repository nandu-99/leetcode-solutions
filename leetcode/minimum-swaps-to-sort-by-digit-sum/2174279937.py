class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        target = sorted(nums, key = lambda x:(sum(int(d) for d in str(x)), x))
        d = {}
        for i in range(len(target)):
            d[target[i]] = i 
        # print(d)
        vis = [False]*len(nums)
        swaps = 0 
        for i in range(len(nums)):
            if vis[i]:continue 
            j = i 
            cycle = 0 
            while not vis[j]:
                vis[j] = True
                cycle+=1
                j = d[nums[j]]
            if cycle>1:
                swaps+=cycle-1 
        return swaps