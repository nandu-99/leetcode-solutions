class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False]*n 
        def dfs(i):
            vis[i] = True 
            for ne in range(n):
                if isConnected[i][ne]==1 and not vis[ne]:
                    dfs(ne)
        c = 0 
        for i in range(n):
            if not vis[i]:
                c+=1 
                dfs(i)
        return c