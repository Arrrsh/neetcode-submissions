"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        start = end = 0
        res = cnt = 0
        while start < len(intervals):
            if starts[start] < ends[end]:
                cnt += 1
                start += 1
            else:
                cnt -= 1
                end += 1
            res = max(res, cnt)
        return res