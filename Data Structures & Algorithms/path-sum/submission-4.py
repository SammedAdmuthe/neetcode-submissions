# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        


        def dfs(node, sum_):
            if not node:
                return False
  
            if not node.left and not node.right:
                return sum_ + node.val == targetSum
                

            return dfs(node.left, sum_ + node.val) or dfs(node.right, sum_ + node.val)

        return dfs(root, 0)