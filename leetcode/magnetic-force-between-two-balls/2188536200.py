class Solution:
    def maxDistance(self, position: list[int], k: int) -> int:
        position.sort()
        def calc(m):
            c = 1 
            last = position[0]
            for i in range(1, len(position)):
                if position[i]-last>=m:
                    c+=1 
                    last = position[i]
                if c>=k: return True 
            return False  

        l = 1 
        h = position[-1]-position[0]
        ans = 0
        while l<=h:
            m = (l+h)//2 
            if calc(m):
                ans = m 
                l = m+1 
            else:
                h = m-1 
        return ans