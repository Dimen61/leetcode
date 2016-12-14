class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        res = 0
        pow_2 = 1
        cc = 0
        while a > 0 or b > 0:

            print('a: {0}; b: {1}'.format(a, b))

            aa = a & 0x1
            bb = b & 0x1
            res += pow_2 * (aa ^ bb ^ cc)
            cc = (aa & bb) | (aa & cc) | (bb & cc)
            pow_2 <<= 1
            
            a >>= 1
            b >>= 1
        if cc > 0:
            res += pow_2
        return res

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        res = 0
        pow_2 = 1
        cc = 0
        for i in range(32):
            aa = pow_2 & a
            bb = pow_2 & b
            if aa ^ bb ^ cc > 0:
                res |= pow_2
            cc = (aa & bb) | (aa & cc) | (bb & cc)
            pow_2 <<= 1
        return res

a = Solution()
print(a.getSum(1, 3))
        