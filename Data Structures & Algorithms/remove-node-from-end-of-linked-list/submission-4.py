# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ''' 
        1 -> 2 -> 3 -> 4
                fast 
        len = 4
        n = 3
        (4 - 2)

        '''
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        slow, fast = head, head

        while fast and n:
            fast = fast.next
            n-=1

        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        print(prev.val)
        prev.next = slow.next
        slow.next = None

        return dummy.next