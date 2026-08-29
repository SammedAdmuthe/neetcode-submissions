# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def checkBalanced(node):
            if not node:
                return [True, 0]

            is_valid_l, l = checkBalanced(node.left)
            is_valid_r, r = checkBalanced(node.right)
            if not is_valid_l or not is_valid_r or abs(l - r) > 1:
                return [False, -1]
            return [True, 1 + max(l, r)]
        
        return checkBalanced(root)[0]