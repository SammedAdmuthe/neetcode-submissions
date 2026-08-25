class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''

            2, 20, 4, 10, 3, 4, 5
                    2    1  3  2  1
        '''
        n = len(nums)
        nums_set = set(nums)
        seen = set()
        res = 0
        for num in nums:
            if num not in seen and (num - 1) not in nums_set:
                count = 0
                curr = num
                while curr in nums_set:
                    count += 1
                    seen.add(num)
                    curr+=1
                
                res = max(res, count)

        return res
