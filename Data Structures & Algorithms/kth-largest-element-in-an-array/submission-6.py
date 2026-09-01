class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        n = len(nums)

        
        def quickSelect(l, r):
            pivot, p = r, l

            for i in range(l, r):

                if nums[i] <= nums[pivot]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
                
                i+=1

            nums[p], nums[pivot] = nums[pivot], nums[p]
            if n - k == p:
                return nums[p]
            elif n-k > p:
                return quickSelect(p+1, r)
            else:
                return quickSelect(l, p-1)

            return -1
            

        return quickSelect(0, n-1)