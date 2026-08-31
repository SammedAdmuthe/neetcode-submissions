# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = [True]
        def isValid(node):
            if not node:
                return [-math.inf, math.inf]

            l_max, l_min = isValid(node.left)
            r_max, r_min = isValid(node.right)

            if (node.val <= l_max or node.val >= r_min):
                res[0] = False
                return [math.inf, -math.inf]

            return [max(node.val, l_max, r_max), min(node.val, l_min, r_min)]


            
        isValid(root)
        return res[0]