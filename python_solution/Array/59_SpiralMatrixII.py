class Solution(object):
    def generateSubMatrix(self, x, y, n, count, matrix):
        """
        :type i: int
        :type j: int
        :type n: int
        :type index: int
        :type matrix: List[List[int]]
        """
        if n == 0: return
        if n == 1:
            matrix[y][x] = count
            return
            
        for i in range(x, x+n):
            matrix[y][i] = count
            count += 1
        for i in range(y+1, y+n-1):
            matrix[i][x+n-1] = count
            count += 1
        for i in range(x, x+n)[::-1]:
            matrix[y+n-1][i] = count
            count += 1
        for i in range(y+1, y+n-1)[::-1]:
            matrix[i][x] = count
            count += 1
            
        subMatrix = self.generateSubMatrix(x+1, y+1, n-2, count, matrix)
        
    
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        
        matrix = [[0]*n for i in range(n)]
        self.generateSubMatrix(0, 0, n, 1, matrix)
        return matrix
        