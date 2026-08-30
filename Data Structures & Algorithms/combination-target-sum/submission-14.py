class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        subList = []
        def getCombination(indx, target):

            if target < 0:
                return

            if target == 0:
                res.add(tuple(subList))
                return



            for i in range(indx, len(nums)):

                subList.append(nums[i])
                getCombination(i, target-nums[i])
                subList.pop()



        getCombination(0, target)
        return [ list(tup) for tup in res]