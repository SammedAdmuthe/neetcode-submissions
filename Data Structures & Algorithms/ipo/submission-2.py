class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_capital = [ (c, p) for c, p in zip(capital, profits)]

        heapq.heapify(min_capital)

        max_capital = []


        for i in range(k):
            
            while min_capital and min_capital[0][0] <= w:
                cap, pro = heapq.heappop(min_capital)
                heapq.heappush(max_capital, -pro)

            if not max_capital:
                return w
            w += -heapq.heappop(max_capital)
        return w

