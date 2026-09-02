class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        latest_indx = {}
        n = len(s)
        for i in range(n):
            latest_indx[s[i]] = i

        # xyxz -> x :2 t:1 z:3

        """
            r < fartest -> r+=1
            r == fartest:

        """
        r = 0
        l = 0
        fartest = 0
        res = []
        while r < n:
            fartest = max(fartest, latest_indx[s[r]])
            if r == fartest:
                res.append((r - l + 1))
                l = fartest + 1
            r+=1

        return res
