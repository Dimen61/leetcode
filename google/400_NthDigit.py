class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1
        token = 9
        num = 1

        while n > token * length:
            n -= token * length
            token *= 10
            length += 1
            num *= 10
            
        s = str(num + (n-1) / length)
        return int(s[(n-1) % length])
            
        
        