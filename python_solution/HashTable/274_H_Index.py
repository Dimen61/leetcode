# Use sorted array to implement a process intuitionly.
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        array = sorted(citations, reverse=True)
        index = citation = 0
        for index, citation in enumerate(array):
            if citation < index + 1: 
                return index
        return len(array)

# Use some iterative trick
class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        num = [0] * (length+1)

        for citation in citations:
            if citation > length:
                num[length] += 1
            else:
                num[citation] += 1

        total = 0
        for i in range(length, -1, -1):
            total += num[i]
            if total >= i:
                return i
        return 0