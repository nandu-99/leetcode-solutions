class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0)+1 
        
        k = list(d.values())
        val = len(arr)//2 
        k.sort(reverse=True)
        if len(k)==len(arr):
            return val
        # print(arr)
        s = 0 
        i = 0 
        while i<len(k):
            s+=k[i]
            i+=1
            # print(s, val)
            if s>=val:
                break 
        return i 