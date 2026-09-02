class Solution:
    def jump(self, nums: List[int]) -> int:
        
        '''
            2 4 1 1 1 1
                      0
        '''
        n = len(nums)
        dp = [0] * n

        for i in range(n-2, -1, -1):
            min_jump = math.inf
            for j in range(i+1, min(i + nums[i] + 1, n)):
                if nums[j]:
                    min_jump = min(min_jump, dp[j])

            dp[i] = min_jump + 1 if min_jump!= math.inf else 0
        print(dp)
        return dp[0]