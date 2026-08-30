class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        n = len(s)
        seen = set()
        res = 0
        for r in range(n):

            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(s[r])
            res = max(res, r - l + 1)

        return res