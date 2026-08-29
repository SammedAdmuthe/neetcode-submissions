class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        n = len(nums)
        def findMax(offset): 
            rob1 = nums[offset]
            rob2 = max(nums[offset], nums[offset+1])

            for i in range(2, n-1):
                rob = max(rob1+nums[i+offset], rob2)
                rob1 = rob2
                rob2 = rob

            return rob2

        return max(findMax(0), findMax(1))