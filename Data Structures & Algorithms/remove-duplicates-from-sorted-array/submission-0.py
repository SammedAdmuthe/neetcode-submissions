class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        dup = 0
        while r < n:
            if nums[l] != nums[r]:
                l+=1
                nums[l], nums[r] = nums[r], nums[l]
            else:
                dup+=1
            r+=1
        
        return n - dup + 1