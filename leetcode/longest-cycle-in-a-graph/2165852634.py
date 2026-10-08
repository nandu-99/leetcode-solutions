class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        vis = [-1]*n 
        ans = -1 
        time = 0 
        for i in range(n):
            if vis[i]!=-1:
                continue 
            curr = i 
            start = time 
            while curr!=-1 and vis[curr]==-1:
                vis[curr] = time 
                time+=1 
                curr = edges[curr]
            if curr!=-1 and vis[curr]>=start:
                ans = max(ans, time-vis[curr])
        return ans