class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subList = []
        nums.sort()
        def getCombination(indx, target):

            if target < 0:
                return

            if target == 0:
                res.append(list(subList))
                return

            i = indx
            while i < len(nums):

                subList.append(nums[i])
                getCombination(i+1, target-nums[i])
                subList.pop()
                while i + 1 < len(nums) and nums[i] == nums[i+1]:
                    i+=1
                i+=1



        getCombination(0, target)
        return res