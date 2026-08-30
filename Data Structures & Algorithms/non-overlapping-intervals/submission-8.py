class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """

            1 ----------5
                2-3   4-5

            
            1 ---- 5 6-7
                3------7


            if curr_interval.start >= prev_interval.end:
                change prev to curr
                continue
            
            if prev_interrval.end > curr_interval.end:
                // skip curr
                continue 

            else
                count+=1
                change prev to curr
        """

        intervals.sort()
        n = len(intervals)
        count = 0
        prev_end = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] >= prev_end:
                prev_end = intervals[i][1]
            else:
                count+=1
                prev_end = min(prev_end, intervals[i][1])

        return count