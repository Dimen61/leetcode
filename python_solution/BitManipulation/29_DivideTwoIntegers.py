class Solution(object):
    def divide(self, dividend, divisor):
        """
        Use left move << to replace multipulation.
        And compose quotient in binary form.

        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000

        if divisor == 0:
            return MAX_INT

        sign = 1 if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            pow2 = 1
            tmp = divisor
            while dividend >= tmp:
                tmp <<= 1
                pow2 <<= 1
            tmp >>= 1
            pow2 >>= 1
            dividend -= tmp
            res += pow2
        
        res = sign * res
        return res if res <= MAX_INT else MAX_INT
                
a = Solution()
print(a.divide(-2147483648, -1))
print(a.divide(-1, -1))