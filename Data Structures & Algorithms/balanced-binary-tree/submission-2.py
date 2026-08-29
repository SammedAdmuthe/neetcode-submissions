# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        isValid = [True]
        def checkBalanced(node):
            if not node:
                return 0

            l = checkBalanced(node.left)
            r = checkBalanced(node.right)
            if abs(l - r) > 1:
                isValid[0] = False
            return 1 + max(l, r)
        checkBalanced(root)
        return isValid[0]