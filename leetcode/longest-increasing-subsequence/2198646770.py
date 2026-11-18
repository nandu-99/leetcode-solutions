class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # d = {}
        # n = len(nums)
        # d = [[-1]*(n+1) for i in range(n+1)]
        # def recur(i, pre):
        #     # if (i, pre) in d:return d[(i, pre)]
        #     if d[i][pre]!=-1:
        #         return d[i][pre]
        #     if i>=len(nums): return 0 
        #     t = 0 
        #     if pre==-1 or nums[pre]<nums[i]:
        #         t = 1+recur(i+1, i)
        #     nt = recur(i+1, pre)
        #     # d[(i,pre)] = max(t, nt)
        #     d[i][pre] = max(t, nt)
        #     return d[i][pre]
        # return recur(0, -1)
        # n = len(nums)
        # d = {}
        # def recur(i):
        #     if i in d:return d[i]
        #     maxi = 1 
        #     for j in range(i+1, n):
        #         if nums[j]>nums[i]:
        #             maxi = max(maxi, 1+recur(j))
        #     d[i] = maxi 
        #     return maxi 

        # ans = 0 
        # for i in range(n):
        #     ans = max(ans, recur(i))
        # return ans
        n = len(nums)
        tails = []
        for num in nums:
            idx = bisect_left(tails, num)
            if idx==len(tails):
                tails.append(num)
            else:
                tails[idx] = num 
        return len(tails)


