# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

            3 2 1
            fiest 3
        """
        res = []

        def inorder(node):
            if not node:
                return


            inorder(node.left)
            res.append(node)
            inorder(node.right)


        inorder(root)
        first, second = None, None

        for i in range(1, len(res)):
            if res[i].val < res[i-1].val and not first:
                first = res[i-1]
                second = res[i]

            elif res[i].val < res[i-1].val:
                second = res[i]
                
           

        first.val, second.val = second.val, first.val


