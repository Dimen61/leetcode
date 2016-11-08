class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        carry = 0
        i = 0
        while i < len(a) and i < len(b):
            aa= int(a[-(i+1)])
            bb = int(b[-(i+1)])
            tmp = aa + bb + carry
            carry = tmp // 2
            res = str(tmp % 2) + res
            i += 1

        while i < len(a):
            aa = int(a[-(i+1)])
            tmp = aa + carry
            carry = tmp // 2
            res = str(tmp % 2) + res
            i += 1
        while i < len(b):
            bb = int(b[-(i+1)])
            tmp = bb + carry
            carry = tmp // 2
            res = str(tmp % 2) + res
            i += 1
        if carry == 1: res = '1' + res
        
        return res

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtyep: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(eval('0b'+a) + eval('0b'+b))[2:]

    def addBinary(self, a, b):
        """
        Recursive way
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a: return b
        elif not b: return a

        aa, bb = int(a[-1]), int(b[-1])
        if aa & bb == 1:
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        if aa | bb == 0:
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'

    def addBinary(self, a, b):
        """
        Iterative way
        :type a: str
        :type b: str
        :rtype: str
        """
        index = 0
        carry = 0
        res = ''
        while index < max(len(a), len(b)) or carry == 1:
            aa = int(a[-1-index]) if index < len(a) else 0
            bb = int(b[-1-index]) if index < len(b) else 0
            tmp = aa + bb + carry
            carry = tmp // 2
            res = str(tmp % 2)+ res
            index += 1
        return res


a = Solution()
assert a.addBinary('1', '111') == '1000'
assert a.addBinary('1010', '1011') == '10101'
print('Done')















