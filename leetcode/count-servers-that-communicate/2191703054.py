class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [0]*n 
        col = [0]*m
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    row[j]+=1 
                    col[i]+=1 
        # print(row)
        # print(col)
        ans = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if row[j]>1 or col[i]>1:
                        ans+=1
        return ans

        