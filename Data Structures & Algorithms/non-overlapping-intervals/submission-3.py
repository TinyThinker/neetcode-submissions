class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        res = 0
        prev_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev_interval[1]:
                prev_interval = intervals[i]
            else:
                res += 1
                if intervals[i][1] < prev_interval[1]:
                    prev_interval = intervals[i]

        return res


