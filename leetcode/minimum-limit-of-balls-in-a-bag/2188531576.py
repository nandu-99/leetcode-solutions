class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def calc(m):
            op = 0 
            for i in nums:
                op+=(i-1)//m 
            return op<=maxOperations
        l = 1 
        h = max(nums)
        while l<h:
            m = (l+h)//2 
            if calc(m):
                h = m 
            else:
                l = m+1
        return l 