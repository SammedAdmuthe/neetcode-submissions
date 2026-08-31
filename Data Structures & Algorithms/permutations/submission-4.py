class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
            1.  2.  3. 
          2. 3  
        3      2
        '''
        seen = set()
        res = []
        subList = []

        n = len(nums)
        def permute(indx):
            if len(subList) == n:
                res.append(list(subList))
                return
            
            for i in range(n):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                subList.append(nums[i])
                permute(i+1)
                subList.pop()
                seen.remove(nums[i])

        permute(0)
        return res

            