# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        maxi = 0 
        tsum = 0 
        def dfs(node, level):
            nonlocal maxi, tsum 
            if not node:return 
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            if maxi<level:
                maxi = level 
                tsum = 0 
            if maxi==level:
                tsum+=node.val 
        dfs(root, 0)
        return tsum