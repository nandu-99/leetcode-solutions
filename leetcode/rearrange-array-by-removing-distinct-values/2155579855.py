class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0)+1 
        unique = sorted(set(nums))
        ans = []
        while d:
            for i in unique:
                if i in d:
                    ans.append(i)
                    d[i]-=1 
                    if d[i]==0:
                        del d[i]
        return ans
