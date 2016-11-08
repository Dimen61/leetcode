# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        merged_intervals = []
        for interval in intervals:
            if not merged_intervals:
                merged_intervals.append(interval)
            elif interval.start <= merged_intervals[-1].end:
                merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)
            else:
                merged_intervals.append(interval)
        return merged_intervals