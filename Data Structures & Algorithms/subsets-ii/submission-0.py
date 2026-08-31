class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_list = []
        nums.sort()
        def findSubset(indx):
            if indx == len(nums):
                res.append(list(sub_list))
                return

            sub_list.append(nums[indx])
            findSubset(indx + 1)
            sub_list.pop()
            while indx + 1 < len(nums) and nums[indx] == nums[indx + 1]:
                indx += 1
            findSubset(indx + 1)

        findSubset(0)
        return res