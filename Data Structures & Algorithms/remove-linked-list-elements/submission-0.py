# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr=head
        dummy=ListNode()
        dummy.next = head
        prev = dummy

        while curr:
            if curr.val == val:
                new_curr = curr.next
                prev.next = curr.next
                curr.next = None
                curr = new_curr
            else: 
                prev = curr
                curr = curr.next

        return dummy.next