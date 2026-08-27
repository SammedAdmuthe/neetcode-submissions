class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_list = []
        def findSubset(indx):
            if indx == len(nums):
                res.append(list(sub_list))
                return

            sub_list.append(nums[indx])
            findSubset(indx + 1)
            sub_list.pop()
            findSubset(indx + 1)

        findSubset(0)
        return res