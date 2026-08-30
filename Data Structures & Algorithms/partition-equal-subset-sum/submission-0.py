class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_%2 != 0:
            return False
        
        target = sum_//2

        dp = {}
        def isPossible(indx, target):
            if indx == len(nums):
                return target == 0

            if (indx, target) in dp:
                return dp[(indx, target)]


            take = isPossible(indx+1, target - nums[indx])
            skip = isPossible(indx+1, target)

            dp[(indx, target)] = take or skip
            return dp[(indx, target)]
            
        return isPossible(0, target)