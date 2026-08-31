class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected = n * (n+1)//2 # 3

        actual = sum(nums)

        return 0 if actual == expected else ((expected - actual))