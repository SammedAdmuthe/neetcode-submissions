class MedianFinder:

    """
        [1, 2, 3]

        [1, 2, 3, 4]
    """

    def __init__(self):
        self.min_heap = [] # 3 5
        self.max_heap = [] # 1 2

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            # insert in minheap
            heapq.heappush(self.min_heap, num)
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        else:
            heapq.heappush(self.max_heap, -num)
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        n = len(self.min_heap) + len(self.max_heap)
        if n % 2 == 0:
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        return -self.max_heap[0]
        