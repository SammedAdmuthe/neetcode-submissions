# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
            root

            if root.val > p.val and root.val < q.val
                return root.val
            elif (root.val > p.val):
                root = root.left
            else:
                root = root.right
        """

        while root:

            if (root.val > p.val and root.val < q.val) or (root.val > q.val and root.val < p.val):
                return root
            elif root.val == p.val or root.val == q.val:
                return root
            elif (root.val > p.val):
                root = root.left
            else:
                root = root.right

