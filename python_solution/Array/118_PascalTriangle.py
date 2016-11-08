class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        current_line = []
        for i in range(numRows):
            if not current_line:
                current_line.append(1)
                triangle.append(current_line)
            else:
                next_line = []
                for j in range(i+1):
                    x = current_line[j-1] if j >= 1 else 0
                    y = current_line[j] if j < i else 0
                    next_line.append(x+y)
                triangle.append(next_line)
                current_line = next_line
        return triangle
                    

a = Solution()
print(a.generate(3))