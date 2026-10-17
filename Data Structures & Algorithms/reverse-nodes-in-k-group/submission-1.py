# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # split the linked list into groups each containing k nodes
        """
            1 -> 2 -> 3
            p -> c
            c. next = prev

        """

        count = 1
        split = []
        curr_head = head
        res = []
        curr = head
        def reverse(curr_head):
            original = curr_head
            dummy = ListNode()
            dummy.next = curr_head
            prev = dummy
            while curr_head:
                new_curr = curr_head.next
                curr_head.next = prev
                prev = curr_head
                curr_head = new_curr

            original.next = None

            return prev

        while curr:
            if count % k == 0:
                next_ = curr.next
                curr.next = None
                before = curr_head
                after = reverse(curr_head)
                split.append((before, after))
                curr = next_
                curr_head = next_
            else:
                curr = curr.next
            count+=1

        

        # for node in split:
        #     while node:
        #         print(node.val)
        #         node = node.next
        #     print("----------")

        if curr_head:
            split.append((None, curr_head ))
        # print(split)
        new_head = split[0][1]
        for i in range(1, len(split)):
            
            if i == 1:
                new_head = split[i-1][1]
            prev_tail, prev_head = split[i-1]
            cur_tail, cur_head = split[i]
            prev_tail.next = cur_head
        
        return new_head

        