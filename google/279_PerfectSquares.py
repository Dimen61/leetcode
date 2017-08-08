class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [100000000] * (n+1)
        f[0] = 0
        for i in range(1, n+1):
            for j in range(1, int(n ** 0.5)+1):
                if j*j <= i:
                    f[i] = min(f[i], f[i-j*j]+1)
                    
        return f[n]
        