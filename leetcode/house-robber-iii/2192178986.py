# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(root):
            if not root:return (0, 0)
            l = dfs(root.left)
            r = dfs(root.right)
            return (root.val+l[1]+r[1], max(l[0], l[1])+max(r[0], r[1]))
        return max(dfs(root))