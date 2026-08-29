# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
            0 1 2 3

            0 1
            3 2
            0 -> 3 -> 1 -> 2


            node1 = 0 <=curr
            node2 = 1 2
            
                0 - > 1
        '''
        def reverse(node):
            prev = None
            curr = node

            while curr:
                new_next = curr.next
                curr.next = prev
                prev = curr
                curr = new_next

            return prev

        def merge (node1, node2):

            """ 
                2,      4
                node1

                6,       8
                node2

            """
            head = node1
            while node1 and node2:
                node1_next = node1.next
                node2_next = node2.next
                node1.next = node2
                node2.next = node1_next

                node2 = node2_next
                node1 = node1_next
            

            return head            

        if not head and not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        slow.next = None
        slow = head


        reversed_ = reverse(fast)

        merge(slow, reversed_)
