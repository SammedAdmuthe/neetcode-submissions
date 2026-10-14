class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        curr_interval_start, curr_interval_end = intervals[0]
        n = len(intervals)
        res = 0
        for i in range(1, n):

            if curr_interval_end <= intervals[i][0]:
                curr_interval_start, curr_interval_end = intervals[i]

                continue
                # res.append([curr_interval_start, curr_interval_end])
                # curr_interval_start, curr_interval_end = intervals[i]

            elif curr_interval_end < intervals[i][1]:
                res += 1
            else:
                res+=1
                curr_interval_end = min(curr_interval_end, intervals[i][1])
        

        return res