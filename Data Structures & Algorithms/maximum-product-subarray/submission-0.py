class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
            currMaxPositive = maxPositive
            maxPositive = max(curr, maxNegative * curr, maxPositive*curr)
            maxNegative = min(curr, maxNegative * curr, maxPositive*curr)
        '''
        best = -math.inf
        maxPositive = 1
        maxNegative = 1
        for curr in nums:
            currMaxPositive = maxPositive
            maxPositive = max(curr, maxNegative * curr, maxPositive*curr)
            maxNegative = min(curr, maxNegative * curr, currMaxPositive*curr)

            best = max(best, maxPositive)

        return best