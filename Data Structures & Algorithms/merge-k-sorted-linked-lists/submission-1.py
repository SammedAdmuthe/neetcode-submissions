# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def merge(l1, l2):
            dummy = ListNode()
            curr = dummy
            curr1, curr2 = l1, l2

            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                elif curr1.val > curr2.val:
                    curr.next = curr2
                    curr2 = curr2.next
                curr = curr.next

            curr.next = curr1 if curr1 else curr2
            return dummy.next



        n = len(lists)
        step = 1
        while step < n:
            j = 0
            while j < n - step:
    
                l1 = lists[j]
                l2 = lists[j+step]
                lists[j] = merge(l1, l2)
                j+=(2* step)
            step*=2

        return lists[0]

       
        
            