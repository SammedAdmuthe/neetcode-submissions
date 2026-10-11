class Node:
    def __init__(self, key = 0, val = 0, next_node = None):
        self.key = key
        self.val = val
        self.next = next_node

class MyHashMap:

    def __init__(self):
        self.map_ = [Node(-1) for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        node = self.map_[key % len(self.map_)]

        while node.next:
            if node.key == key:
                node.val = value
                return
            node = node.next

        if node.key == key:
            node.val = value
            return
        node.next = Node(key, value)

    def get(self, key: int) -> int:
        curr = self.map_[key % len(self.map_)]

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

        return -1

            

    def remove(self, key: int) -> None:

        node = self.map_[key % len(self.map_)]
        prev = node
        curr = node.next

        while curr:
            if curr.key == key:
                prev.next = curr.next
                curr.next = None

                return

            prev = curr
            curr = curr.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)