class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        n = len(nums)
        triplets = set()
        for i in range(n-2):
            
            target = -1 * nums[i]
            seen = {}
            for j in range(i+1, n):
                if target - nums[j] in seen:
                    k = seen[target - nums[j]]
                    to_sort = [nums[i], nums[k], nums[j]]

                    triplets.add(tuple(sorted(to_sort)))
                seen[nums[j]] = j

        return list(triplets)