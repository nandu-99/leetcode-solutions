# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        def inorder(node, vals):
            if not node:return 
            inorder(node.left, vals)
            vals.append(node.val)
            inorder(node.right, vals)
        def build(vals, l, r):
            if l>r:return None 
            m = (l+r)//2 
            node = TreeNode(vals[m])
            node.left = build(vals, l, m-1)
            node.right= build(vals, m+1, r)
            return node 
        vals = []
        inorder(root, vals)
        return build(vals, 0, len(vals)-1)