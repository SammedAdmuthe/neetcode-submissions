# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        curr = root
        par = root


        while curr:
            if curr.val > val:
                par = curr
                curr= curr.left
            else:
                par = curr
                curr = curr.right

        new_node = TreeNode(val)
        if val > par.val:
            par.right = new_node
        else:
            par.left = new_node

        return root