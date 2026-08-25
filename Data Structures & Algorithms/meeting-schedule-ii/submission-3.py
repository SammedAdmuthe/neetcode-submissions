"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        n = len(intervals)

        q = []
        res = 0
        print(n)

        for interval in intervals:
            while q and q[0] <= interval.start:
                heapq.heappop(q)
            heapq.heappush(q, interval.end)
            res = max(res, len(q))

        return res