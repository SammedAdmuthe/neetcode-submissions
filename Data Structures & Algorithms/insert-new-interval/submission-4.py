class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)

        intervals.sort(key = lambda x:x[0])

        res = []
        new_x, new_y = newInterval
        
        for i in range(0, n):
            if intervals[i][0] > new_y:
                res.append([new_x, new_y])
                new_x = intervals[i][0]
                new_y = intervals[i][1]
            elif intervals[i][1] < new_x:
                res.append(intervals[i])
            else:
                new_x = min(new_x, intervals[i][0])
                new_y = max(new_y, intervals[i][1])

        res.append([new_x, new_y])

        return res