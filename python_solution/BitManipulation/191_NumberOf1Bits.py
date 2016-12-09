class Solution(object):
    def hammingWeight(self, n):
        """
        Use the trick of turning the rightest 1 to 0.
        The trick: n & (n-1)
        
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += 1
            n &= n-1
        return res