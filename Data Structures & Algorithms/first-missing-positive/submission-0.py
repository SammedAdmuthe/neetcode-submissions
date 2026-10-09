class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        set_ = set(nums)

        i = 1

        while True:

            if i not in set_:
                return i

            i+=1
        return -1