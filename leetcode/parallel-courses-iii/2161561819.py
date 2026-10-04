class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        graph = [[]for i in range(n+1)]
        indegree = [0]*(n+1)
        maxTime = [0]*(n+1)
        for u, v in relations:
            graph[u].append(v)
            indegree[v]+=1
        queue = []
        for i in range(1, n+1):
            if indegree[i]==0:
                queue.append(i)
                maxTime[i] = time[i-1]  
        while queue:
            u = queue.pop(0)
            for v in graph[u]:
                maxTime[v] = max(maxTime[v], maxTime[u]+time[v-1])
                indegree[v]-=1 
                if indegree[v]==0:queue.append(v)
        return max(maxTime)