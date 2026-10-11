class Node:
    def __init__(self, val = 0, next_node = None, prev_node = None):
        self.val = val
        self.next = next_node
        self.prev = prev_node

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        curr = self.head.next

        while curr.next:
            if index == 0:
                return curr.val
            index-=1
            curr = curr.next

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.prev = self.head
        next_ = self.head.next
        self.head.next = new_node
        new_node.next = next_
        next_.prev = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.tail
        _prev = self.tail.prev 
        self.tail.prev = new_node
        new_node.prev = _prev
        _prev.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next

        while curr.next:
            if index == 0:
                #add node here
                new_node = Node(val)
                prev_ = curr.prev

                prev_.next = new_node
                new_node.prev = prev_

                curr.prev = new_node
                new_node.next = curr

                return
            index-=1

            curr = curr.next
        if index == 0:
            self.addAtTail(val)

            

    def deleteAtIndex(self, index: int) -> None:
        
        curr = self.head.next

        while curr.next:
            if index == 0:
                prev_ = curr.prev
                next_ = curr.next

                prev_.next = next_
                next_.prev = prev_
                curr.next = None
                curr.prev = None
                return
            index-=1
            curr = curr.next

        return -1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)