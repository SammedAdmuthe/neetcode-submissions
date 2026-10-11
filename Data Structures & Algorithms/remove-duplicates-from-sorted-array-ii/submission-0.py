class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''


                1 1 1 2 2 3
                l = 0 
                r = 3
                k - l > 2
                 l+=2

        '''
        l = 0
        r = 0
        while r < len(nums):
            k = r
            while r < len(nums) and nums[k] == nums[r]:
                r+=1

            if r - k >= 2:
                nums[l] = nums[k]
                nums[l+1] = nums[k]
                l+=2
            else:
                nums[l] = nums[k]
                l+=1

        return l