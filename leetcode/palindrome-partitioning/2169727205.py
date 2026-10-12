class Solution:
    def partition(self, a: str) -> list[list[str]]:
        ans = []
        def recur(i, curr):
            if i==len(a):
                ans.append(curr[:])
                return 
            for j in range(i+1, len(a)+1):
                if a[i:j]==a[i:j][::-1]:
                    curr.append(a[i:j])
                    recur(j, curr)
                    curr.pop()
        recur(0, [])
        return ans