class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def findPossibleWays(indx, target):

            if indx == len(nums):
                if target == 0:
                    return 1
                return 0

            if (indx, target) in dp:
                return dp[(indx, target)]

            dp[(indx, target)] = (
                findPossibleWays(indx+1, target - nums[indx])
                + findPossibleWays(indx+1, target + nums[indx])
            )
            return dp[(indx, target)]

        return findPossibleWays(0, target)
        