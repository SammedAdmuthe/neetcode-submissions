class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            1, 2 -> min(a[0], a[1])
            1, 2, 3 -> min (dp[0] + cost, dp[2] + cost)

        '''

        dp = [0] * (len(cost) + 1)

        dp[0] = 0
        dp[1] = 0


        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[len(cost)]