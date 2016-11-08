class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        tmp_str = ''
        legal_symbols = [chr(x) for x in range(ord('0'), ord('9')+1)] + ['-', '+']
        for c in str:
            if c in legal_symbols:
                tmp_str += c
            else: break

        try:
            res = int(tmp_str)
            MIN_INT = -1 * 2 ** 31
            MAX_INT = 2 ** 31 - 1
            return min(res, MAX_INT) if res >= 0 else max(res, MIN_INT)
        except ValueError:
            return 0
        return 0






a = Solution()
print(a.myAtoi('-0012a42'))
print(a.myAtoi('+-2'))
print(a.myAtoi("  -0012a42"))
print(a.myAtoi("2147483648"))
