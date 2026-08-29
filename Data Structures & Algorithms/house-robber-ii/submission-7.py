class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        n = len(nums)
        def findMax(offset): 
            dp = [0] * (n - 1)
            dp[0] = nums[offset]
            dp[1] = max(nums[offset], nums[offset+1])

            for i in range(2, n-1):
                dp[i] = max(dp[i-2]+nums[i+offset], dp[i-1])

            return dp[(n - 2)]

        return max(findMax(0), findMax(1))