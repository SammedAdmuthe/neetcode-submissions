class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = defaultdict(int)
        l = 0

        def isValid(tracker):

            # AABCD K = 3
            # A: 3 B: 1 C : 1 D: 1
            sum_ = 0
            max_value = -math.inf
            for key, val in tracker.items():
                sum_ += val
                max_value = max (max_value, val)

            return k >= (sum_ - max_value)

        res = 0
        for r in range(len(s)):
            tracker[s[r]] += 1
            while l < r and not isValid(tracker):
                tracker[s[l]] -= 1
                l+=1

            res = max(res, (r-l+1))
            
        return res