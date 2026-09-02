class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_jump = 0
        for i in range(n - 1):
            max_jump = max(max_jump, i + nums[i])
            if max_jump <= i:
                return False
        
        return True
