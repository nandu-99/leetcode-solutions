class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        vis = [-1]*n
        def bfs(i):
            queue = deque([i])
            vis[i] = 0
            while queue:
                node = queue.popleft()
                for ne in graph[node]:
                    if vis[ne]==-1:
                        vis[ne] = 1-vis[node]
                        queue.append(ne)
                    elif vis[ne]==vis[node]:
                        return False 
            return True 
        
        for i in range(n):
            if vis[i]==-1:
                if bfs(i)==False:
                    return False 
        return True
