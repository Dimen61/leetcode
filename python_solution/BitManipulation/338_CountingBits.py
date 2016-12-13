class Solution(object):
    def countBits(self, num):
        """
        Dynamic programming

        :type num: int
        :rtype: List[int]
        """
        f = [0] * (num+1)
        for i in range(num+1):
            if 2*i + 1 <= num:
                f[2*i+1] = f[i] + 1
            if 2*i <= num:
                f[2*i] = f[i]
        return f

        