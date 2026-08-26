import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        top_k = []
        n = len(nums)
        freq = defaultdict(int)
        for i in range(n):
            freq[nums[i]] += 1

        for num, count in freq.items():
            heapq.heappush(top_k, (count, num))

            if len(top_k) == k + 1:
                heapq.heappop(top_k)
        
        return [val for _, val in top_k]
