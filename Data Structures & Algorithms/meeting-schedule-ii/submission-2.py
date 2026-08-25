"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
'''
    [1, 4], [2, 4], [3, 4], [5, 10]
    4, 4, 10

'''
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
            0 - start.      10, 40
            5 - start
        

        '''
        
        intervals.sort(key = lambda x : x.start)
        n = len(intervals)

        heap = []
        res = 0
        for interval in intervals:
            si, ei = interval.start, interval.end
            while heap and heap[0] <= si:

                heapq.heappop(heap)
            heapq.heappush(heap, ei)
            res = max(res, len(heap))

        return res