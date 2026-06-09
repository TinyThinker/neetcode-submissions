class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        res = 0
        prev_interval = intervals[0]
        for start, end  in intervals[1:]:
            if start >= prev_interval[1]:
                prev_interval = [start, end]
            else:
                res += 1
                if end < prev_interval[1]:
                    prev_interval = [start, end]

        return res


