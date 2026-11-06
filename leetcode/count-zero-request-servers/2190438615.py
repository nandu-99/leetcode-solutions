class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs = sorted(logs, key=lambda x:x[1])
        for i in range(len(queries)):
            queries[i] = (queries[i], i)
        queries = sorted(queries)
        d = {}
        ans = [0]*len(queries)
        l, r = 0, 0 
        active = 0 
        for query, i in queries:
            s = query-x 
            while r<len(logs) and logs[r][1]<=query:
                server = logs[r][0]
                if d.get(server, 0)==0:
                    active+=1 
                d[server] = d.get(server, 0)+1 
                r+=1 
            while l<r and logs[l][1]<s:
                server = logs[l][0]
                d[server]-=1 
                if d[server]==0:
                    active-=1
                l+=1 
            ans[i] = n-active 
        return ans



        