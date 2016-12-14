class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #        01234567890123456789012345678901
        mask = 0b01010101010101010101010101010101

        return num > 0 and num & (num-1) == 0 and mask & num > 0
      

a = Solution()  
print(a.isPowerOfFour(16))
