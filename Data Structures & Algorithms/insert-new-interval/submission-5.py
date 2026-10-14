class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()

        curr_interval_start, curr_interval_end = newInterval
        n = len(intervals)
        res = []
        for i in range(n):

            if curr_interval_start > intervals[i][1]:
                res.append(intervals[i])
            elif curr_interval_end < intervals[i][0]:
                res.append([curr_interval_start, curr_interval_end])
                curr_interval_start, curr_interval_end = intervals[i]
            else:
                curr_interval_start = min(curr_interval_start, intervals[i][0])
                curr_interval_end = max(curr_interval_end, intervals[i][1])
        
        res.append([curr_interval_start, curr_interval_end])

        return res