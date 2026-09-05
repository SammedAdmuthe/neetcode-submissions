class Node:
    def __init__(self, key, val, next_ = None, prev_ = None):
        self.key = key
        self.val = val
        
        self.next = None if not next_ else next_
        self.prev = None if not prev_ else prev_

class LRUCache:
    """
        n = 5
        [1, 2 ,3 ,4, 5]


        key -> value

    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # int -> node

        self.most_recent = Node(-1, -1)
        self.least_recent = Node(-1, -1)
        self.most_recent.prev = self.least_recent
        self.least_recent.next = self.most_recent

        # lru <-> mru

    def get(self, key: int) -> int:
        # every get call updates key to make it most recently
        if key in self.cache:
            self.makeMostRecent(self.cache[key])
            return self.cache[key].val
        return -1

    def detachNode(self, curr):
        if not curr.next and not curr.prev:
            return curr
        prev_ = curr.prev
        next_ = curr.next
        prev_.next = next_
        next_.prev = prev_
        curr.next = None
        curr.prev = None
        return curr

    def makeMostRecent(self, curr):
        curr = self.detachNode(curr)

        prev_ = self.most_recent.prev

        prev_.next = curr
        curr.prev = prev_
        curr.next = self.most_recent
        self.most_recent.prev = curr


    def evict(self):
        to_be_evicted = self.least_recent.next
        curr = self.detachNode(to_be_evicted)
        del self.cache[curr.key]

    def put(self, key: int, value: int) -> None:
        # after put we put key at position to most recently
        curr_node = None
        if key in self.cache:
            curr_node = self.cache[key]
            curr_node.val = value
        
        elif len(self.cache) == self.capacity:
            #evict least recently used
            self.evict()
            curr_node = Node(key, value)
        else:
            curr_node = Node(key, value)

        self.cache[key] = curr_node
        self.makeMostRecent(curr_node)

        #push the current key as most recently used
        
