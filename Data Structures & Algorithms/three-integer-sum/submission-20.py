class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        triplets = []
        i = 0
        while i < (n-2):
            
            target = -1 * nums[i]
            l, r = i+1, n-1
            while l < r:
                sum_ = nums[l] + nums[r]

                if sum_ > target:
                    r-=1
                elif sum_ < target:
                    l+=1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1

            i+=1
            while i < (n-2) and nums[i] == nums[i-1]:
                i+=1
            
        return triplets