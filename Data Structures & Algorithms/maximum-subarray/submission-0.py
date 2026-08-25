class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        '''
        '''
        max_so_far = 0
        res = -float('inf')
        for num in nums:
            max_so_far += num
            res = max(max_so_far, res)
            if max_so_far < 0:
                max_so_far = 0

        return res 