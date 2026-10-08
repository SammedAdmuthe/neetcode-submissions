class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)

        count[0] = 1
        prefixSum = 0
        res = 0
        for num in nums:
            prefixSum+=num

            if prefixSum % k in count:
                res += count[prefixSum % k]

            count[prefixSum % k] +=1
        
        return res