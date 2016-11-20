class Solution(object):
    def hIndex(self, citations):
        """
        Use binary search with hard thinking.
        The best way to comprehend how things go on is to draw sketch.

        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        left, right = 0, length-1
        while left <= right:
            mid = left + (right-left) // 2
            if (citations[mid] == length-mid): return citations[mid]
            elif citations[mid] < length-mid:
                left = mid + 1
            elif citations[mid] > length-mid:
                right = mid - 1
        return length - left
