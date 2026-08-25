class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        n = len(intervals)
        new_i, new_j = intervals[0]
        res = []
        for i in range(1, n):
            if intervals[i][0] > new_j:
                res.append([new_i, new_j])
                new_i, new_j = intervals[i]
            else:
                new_i = min(new_i, intervals[i][0])
                new_j = max(new_j, intervals[i][1])

        res.append([new_i, new_j])
        return res