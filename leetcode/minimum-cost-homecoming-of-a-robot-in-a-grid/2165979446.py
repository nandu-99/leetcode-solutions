class Solution:
    def minCost(self, startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
        # d = {} 

        # def recur(i, j):
        #     if (i, j)==tuple(homePos):return 0 
        #     if (i, j) in d:return d[(i, j)]
        #     ans = float('inf')
        #     hr, hc = homePos[0], homePos[1]
        #     if i<hr:
        #         ans = min(ans, rowCosts[i+1]+recur(i+1, j))
        #     if i>hr:
        #         ans = min(ans, rowCosts[i-1]+recur(i-1, j))
        #     if j<hc:
        #         ans = min(ans, colCosts[j+1]+recur(i, j+1))
        #     if j>hc:
        #         ans= min(ans, colCosts[j-1]+recur(i, j-1))
        #     d[(i, j)] = ans 
        #     return ans 
        # return recur(startPos[0], startPos[1])

        sr, sc = startPos[0], startPos[1]
        hr, hc = homePos[0], homePos[1]
        ans = 0 
        if sr<hr:
            for i in range(sr+1, hr+1):
                ans+=rowCosts[i]
        else:
            for i in range(sr-1, hr-1, -1):
                ans+=rowCosts[i]
        if sc<hc:
            for i in range(sc+1, hc+1):
                ans+=colCosts[i]
        else:
            for i in range(sc-1, hc-1, -1):
                ans+=colCosts[i]
        return ans