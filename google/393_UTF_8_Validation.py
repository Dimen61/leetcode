class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def getCharType(char):
            if char & 128 == 0:
                return 0
            elif char & 64 == 0:
                return 4
            elif char & 32 == 0:
                return 1
            elif char & 16 == 0:
                return 2
            elif char & 8 == 0:
                return 3
            else:
                return -1
            
        seq_num = 0
        for x in data:
            t = getCharType(x)
            if t == -1:
                return False
            elif 0 <= t <= 3:
                if seq_num == 0:
                    seq_num = t
                else: return False
            elif t == 4:
                seq_num -= 1
                if seq_num < 0: return False
                    
        return seq_num == 0
        
        
        