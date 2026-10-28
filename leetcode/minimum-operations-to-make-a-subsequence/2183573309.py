class Solution:
    def minOperations(self, target: list[int], arr: list[int]) -> int:
        def lis(arr):
            larr = []
            for x in arr:
                i = bisect_left(larr, x)
                if i==len(larr):
                    larr.append(x)
                else:
                    larr[i]= x 
            return len(larr)
            # n = len(arr)
            # d = [[-1]*n for i in range(n)]
            # def recur(i, pre):
            #     if i==n:return 0 
            #     if d[i][pre]!=-1:return d[i][pre]
            #     t = 0 
            #     if pre==-1 or arr[i]>arr[pre]:
            #         t = 1+recur(i+1, i)
            #     nt = recur(i+1, pre)
            #     d[i][pre] = max(t, nt)
            #     return d[i][pre]
            # return recur(0, -1)
        d = {}
        for i in range(len(target)):
            d[target[i]] = i
        
        newarr = []
        for i in arr:
            if i in d:
                newarr.append(d[i])
        
        l = lis(newarr)
        return len(target)-l