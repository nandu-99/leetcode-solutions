class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        vis = set()

        def dfs(r, c, k):
            if k==len(word):return True 
            if not (0<=r<m) or not (0<=c<n) or (r, c) in vis or board[r][c]!=word[k]:
                return False 
            vis.add((r, c))
            res = dfs(r+1, c, k+1) or dfs(r-1, c, k+1) or dfs(r, c+1, k+1) or dfs(r, c-1, k+1)
            vis.remove((r, c))
            return res


        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True 
        return False