class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # input: list of non-overlapping intervals
        # where interval[i][0] is the start of the interval
        # and   interval[i][1] is the end of the interval.
        # Sorted ascending order of the start.
        #
        # I have another newInterval which needs to be inserted in the array of intervals.
        # Invariant, after insertion the intervals remain sorted in ascending order and there
        # will not be overlapping intervals. (this means we may have to merge)
        #
        # So we have a few cases here.
        # An interval can be fully before the current interval.
        # An interval can be fully after the current interval
        # An interval can fit fully between the current interval and the next one.
        # The interval overlaps and we need to merge the interval.  

        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        res.append(newInterval)
        return res

