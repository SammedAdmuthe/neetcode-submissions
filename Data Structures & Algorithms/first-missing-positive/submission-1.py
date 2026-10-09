class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i, num in enumerate(nums):
            if nums[i] < 0:
                nums[i] = 0

        '''
            [-2, -1, 1, 2, 3, 7]
            [0, 0, 4, 2, -3, 7]
            []
        '''

        for i, num in enumerate(nums):
            if abs(nums[i]) >= 1 and abs(nums[i]) <= len(nums):
                if nums[abs(nums[i]) - 1] == 0:
                    nums[abs(nums[i]) - 1] = -1 * (len(nums) + 1)

                elif nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1

        print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1

        return len(nums) + 1
