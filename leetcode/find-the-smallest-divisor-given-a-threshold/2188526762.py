class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def calc(m):
            s = 0 
            for i in nums:
                s+=math.ceil(i/m)
            return s<=threshold
        l = 1 
        h= max(nums)
        while l<h:
            m = (l+h)//2 
            if calc(m):
                h = m 
            else:
                l = m+1 
        return l 