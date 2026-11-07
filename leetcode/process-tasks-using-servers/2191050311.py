class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = []
        for i in range(len(servers)):
            free.append((servers[i], i))
        heapq.heapify(free)
        busy = []
        ans = []
        time = 0 
        for j in range(len(tasks)):
            task = tasks[j]
            time = max(time, j)
            while busy and busy[0][0]<=time:
                a, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            if not free:
                time = busy[0][0]
                while busy and busy[0][0]<=time:
                    a, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))
            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (time+task, w, i))
        return ans
