class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        def dist(start):
            d = {}
            curr = start 
            c = 0 
            while curr!=-1 and curr not in d:
                d[curr] = c 
                c+=1 
                curr = edges[curr]
            return d 
        
        d1 = dist(node1)
        d2 = dist(node2)
        mini = float('inf')
        ans = -1
        for i in d1:
            if i in d2:
                di = max(d1[i], d2[i])
                if di<mini or (di==mini and i<ans):
                    mini = di 
                    ans = i
        return ans
