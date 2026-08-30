# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        


        def isSimilar(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            

            if node1.val != node2.val:
                return False
            elif not isSimilar(node1.left, node2.left):
                return False
            elif not isSimilar(node1.right, node2.right):
                return False

            return True


        return isSimilar(p, q)