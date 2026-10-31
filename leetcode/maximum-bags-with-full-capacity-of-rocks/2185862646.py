class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        diff = []
        for i in range(len(capacity)):
            diff.append(capacity[i]-rocks[i])
        
        diff.sort()
        if sum(diff)<=additionalRocks: return len(capacity)

        i = 0 
        while additionalRocks>0 and i<len(diff):
            if additionalRocks>=diff[i]:
                additionalRocks-=diff[i]
                diff[i] = 0 
            i+=1 
        
        c = 0 
        for i in diff:
            if i==0:
                c+=1 
        return c 