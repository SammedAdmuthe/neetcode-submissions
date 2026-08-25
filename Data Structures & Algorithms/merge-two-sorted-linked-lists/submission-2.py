# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        node1 = list1
        node2 = list2

        def merge(node1, node2, node):
            if node1.val <= node2.val:
                node.next = node1
                node1 = node1.next
                
            elif node1.val > node2.val:
                node.next = node2
                node2 = node2.next

            return [node1, node2, node.next]

        dummy_head = ListNode(-1)
        node = dummy_head
        while node1 != None and node2 != None:
            node1, node2, node = merge(node1, node2, node)
            

        if node1:
            node.next = node1
        elif node2:
            node.next = node2

        return dummy_head.next




