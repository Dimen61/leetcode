class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        current_row = []
        for i in range(rowIndex):
            if not current_row:
                current_row.append(1)
            else:
                next_row = []
                for j in range(i+1):
                    x = current_row[j-1] if j >= 1 else 0
                    y = current_row[j] if j < i else 0
                    next_row.append(x+y)
                current_row = next_row
                    
        return current_row
        
a = Solution()
print(a.getRow(3))