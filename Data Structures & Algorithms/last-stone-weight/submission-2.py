import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            stone1, stone2 = -heapq.heappop(heap), -heapq.heappop(heap)

            if stone1 < stone2:
                heapq.heappush(heap, -(stone2 - stone1))
            if stone2 < stone1:
                heapq.heappush(heap, -(stone1 - stone2))

        return -heap[0] if heap else 0