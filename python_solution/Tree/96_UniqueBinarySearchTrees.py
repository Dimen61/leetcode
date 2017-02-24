# Use Catalan number
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        lst = list(range(1, n+2))
        for i in range(1, n+1):
            ans *= (n+i)
            while lst and ans % lst[-1] == 0:
                ans //= lst[-1]
                lst.pop()
        return ans