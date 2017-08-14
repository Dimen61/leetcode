class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        max_area = 0
        f = [[0 for j in range(m+1)] for i in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if matrix[i][j] == '0': continue
                
                f[i][j] = min(f[i][j+1], f[i+1][j])
                if matrix[i+f[i][j]][j+f[i][j]] == '1':
                    f[i][j] += 1
                
                max_area = max(max_area, f[i][j] * f[i][j])
                
        return max_area
        
                
                
        
        
        
        