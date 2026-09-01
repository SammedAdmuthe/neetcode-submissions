# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = [-math.inf]
        def dfs(node):

            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            res[0] = max(res[0], node.val + l + r, node.val, node.val + l, node.val + r)
            return max(node.val, node.val + l, node.val+r)

        dfs(root)

        return res[0]