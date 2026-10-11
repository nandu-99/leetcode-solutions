class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for i in range(n)]
        for u,v, w in flights:
            graph[u].append((v, w))
        queue = [(0, src, 0)]
        vis = {(src,0):0}
        while queue:
            curr, city, stops = heapq.heappop(queue)
            if city==dst: return curr 
            if stops<=k:
                for neighbor, neighbor_curr in graph[city]:
                    total = curr+neighbor_curr 
                    if (neighbor, stops+1) not in vis or total<vis[(neighbor, stops+1)]:
                        vis[(neighbor, stops+1)] = total 
                        heapq.heappush(queue, (total, neighbor, stops+1))
        return -1