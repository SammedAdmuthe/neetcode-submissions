"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tracker = defaultdict(Node)
        if not head:
            return head
        curr = head
        while curr:
            random_node = curr.random
            next_node = curr.next
            new_random_node = tracker.get(random_node, None)

            
            if random_node and not new_random_node:
                new_random_node = Node(random_node.val)
                tracker[random_node] = new_random_node

            new_next_node = tracker.get(next_node, None)
            if next_node and not new_next_node:
                new_next_node = Node(next_node.val)
                tracker[next_node] = new_next_node

            newCurr = tracker.get(curr, None)
            if not newCurr:
                newCurr = Node(curr.val, new_next_node, new_random_node)
                tracker[curr] = newCurr
            
            newCurr.val = curr.val
            newCurr.next = new_next_node
            newCurr.random = new_random_node
            tracker[curr] = newCurr
            newCurr = newCurr.next
            curr = curr.next
        return tracker[head]