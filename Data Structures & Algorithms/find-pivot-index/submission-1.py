class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
            sum_left == sum_right
        '''
        sum_ = sum(nums)

        left = 0
        right = sum_

        for i in range(len(nums)):
            num = nums[i]
            right-=num
            if left == right:
                return i

            left+=num
            

        return len(nums) - 1 if left == right else -1