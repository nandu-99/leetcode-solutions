class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        even = 1 
        odd = 0 
        prefix = 0 
        for i in arr:
            prefix+=i 
            if prefix%2==0:
                even+=1 
            else:
                odd+=1 
        return (odd*even)%(10**9+7)