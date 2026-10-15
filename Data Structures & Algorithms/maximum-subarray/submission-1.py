class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        '''
        '''
        max_so_far = 0
        res = -float('inf')
        max_ = 0
        for num in nums:
            max_ = max(max_+num, num)
            res = max(max_, res)

        return res 