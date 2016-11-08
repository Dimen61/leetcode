class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = '1'
        for i in range(n-1):
            x = ''
            num = 0
            next_seq = ''
            for c in seq:
                if not x:
                    x = c
                    num = 1
                elif c == x: 
                    num += 1
                else:
                    next_seq += str(num) + x
                    x = c
                    num = 1
            next_seq += str(num) + x
            seq = next_seq
        return seq
            
        