# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        prev = head
        curr = head.next
        # 1 -> 2 -> 3
        # prev -> curr -> new_curr
        # curr.next = prev
        # prev = curr
        while curr:
            new_curr = curr.next
            curr.next = prev
            prev = curr
            curr = new_curr
        head.next = None
        return prev
        