
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1

        res = max_k
        l, r = min_k, max_k
        def canEat(k, h):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours <= h


        while l <= r:

            k = l + (r-l)//2
            if canEat(k, h):
                res = k
                r = k - 1
            else:
                l = k + 1

        return res
