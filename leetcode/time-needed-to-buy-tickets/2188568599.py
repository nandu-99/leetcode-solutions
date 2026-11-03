class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        queue = deque()
        for i in range(len(tickets)):
            queue.append((tickets[i], i))
        c = 0 
        while queue:
            v, i = queue.popleft()
            if v-1>0:
                queue.append((v-1, i))
                c+=1
            if v-1==0:
                c+=1
            if v-1==0 and i==k:
                return c 
            
    