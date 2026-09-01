class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_map = defaultdict(int)
        s2_map = defaultdict(int)
        for c in s1:
            s1_map[c] += 1

        def containsPermutation(s1_map, s2_map):
            for key, val in s1_map.items():
                if key not in s2_map:
                    return False
                
                if s2_map[key] != val:
                    return False
            return True

        m = len(s1)
        n = len(s2)
        l = 0
        for r in range(n):
            s2_map[s2[r]] += 1

            if r - l + 1 == m:
                if containsPermutation(s1_map, s2_map):
                    return True
                s2_map[s2[l]] -=1
                l+=1

        return False