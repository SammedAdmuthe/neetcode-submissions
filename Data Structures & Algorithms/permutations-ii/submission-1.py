class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        seen = set()
        res = []
        sub_list = []
        nums.sort()
        def permute():

            if len(sub_list) == len(nums):
                res.append(list(sub_list))
                return

            i = 0
            while i < len(nums):
                if i in seen:
                    i+=1
                    continue

                seen.add(i)
                sub_list.append(nums[i])
                permute()
                seen.remove(i)
                sub_list.pop()

                while i+1 < len(nums) and nums[i] == nums[i+1]:
                    i+=1

                i+=1

        permute()
        return res