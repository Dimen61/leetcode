# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals: return [newInterval]
        elif newInterval.end < intervals[0].start:
            return [newInterval] + intervals
        elif newInterval.start > intervals[-1].end:
            return intervals + [newInterval]

        merged_intervals = []
        index = 0
        length = len(intervals)
        flag = False
        while index < length:
            if intervals[index].end < newInterval.start:
                merged_intervals.append(intervals[index])
                index += 1
            elif intervals[index].end >= newInterval.start and not flag:
                flag = True
                if intervals[index].start > newInterval.end:
                    merged_intervals.append(newInterval)
                    continue
                intervals[index].end = max(intervals[index].end, newInterval.end)
                intervals[index].start = min(intervals[index].start, newInterval.start)
                merged_intervals.append(intervals[index])
                index += 1
                while index < length and intervals[index].start <= merged_intervals[-1].end:
                    merged_intervals[-1].end = max(merged_intervals[-1].end, intervals[index].end)
                    index += 1
            else:
                merged_intervals.append(intervals[index])
                index += 1

        return merged_intervals
