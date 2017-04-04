class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return [0]
        elif n == 1:
            return [0, 1]
        else:
            seq = self.grayCode(n-1)
            return seq + [x+2**(n-1) for x in seq][::-1]
        