class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits interger min
        MAX_INT = 0x7FFFFFFF
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= MAX_INT else ~((a-1) ^ mask) + 1

a = Solution()
print(a.getSum(-1, -5))
        