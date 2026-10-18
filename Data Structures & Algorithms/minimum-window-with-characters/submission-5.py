class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        if len(s) < len(t):
            return ""
        source_map = defaultdict(int)
        target_map = defaultdict(int)

        for i in range(len(t)):
            target_map[t[i]] +=1

        def isMatching():
            for c in target_map.keys():
                if c not in source_map or source_map[c] < target_map[c]:
                    return False
            return True

        need, have = len(target_map), 0
        n = len(s)
        l = 0
        len_ = math.inf
        start = -1
        for r in range(n):
            source_map[s[r]]+=1
            if source_map[s[r]] == target_map[s[r]]:
                have+=1
            while l <= r and need == have:
                if len_ > r - l:
                    len_ = r - l
                    start = l
                source_map[s[l]]-=1

                if s[l] in target_map and source_map[s[l]] < target_map[s[l]]:
                    have-=1
                l+=1

        return s[start:start + len_ + 1] if start != -1 else ""