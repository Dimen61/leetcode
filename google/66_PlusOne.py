class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = digits[:]
        carry = False
        for i in range(len(res))[::-1]:
            if i == len(res) - 1 or carry:
                res[i] = (res[i] + 1) % 10
                carry = (res[i] == 0)
        
        if carry:
            return [1] + res
        else:
            return res
                
            
            