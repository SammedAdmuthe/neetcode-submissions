class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        max_freq = 0
        for num in nums:
            freq[num] += 1
            max_freq = max(max_freq, freq[num])
        

        bucket = [[] for _ in range(max_freq + 1)]

        for key, val in freq.items():
            bucket[val].append(key)

        res = []
        for i in range(max_freq, -1, -1):
    
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
            





        
