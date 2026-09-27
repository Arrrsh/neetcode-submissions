class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        i = 1
        while i < len(intervals):
            cur_start, cur_end = intervals[i]
            lastEnd = res[-1][1]
            if cur_start <= lastEnd:
                res[-1][1] = max(cur_end, lastEnd)
            else:
                res.append([cur_start, cur_end])
            i += 1
        return res