class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            [1, 2, 3, 2, 2]
            [-1, -2, -3, ]
        '''
        n = len(nums)

        for i in range(n):
            if nums[abs(nums[i])-1] < 0:
                return abs(nums[i])
            
            nums[abs(nums[i])-1] = -1 * nums[abs(nums[i])-1]

        return -1