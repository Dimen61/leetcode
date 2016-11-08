class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        if n == 0: return [[] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = str(matrix[i][j])
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    for k in range(m):
                        if matrix[k][j] != '0': matrix[k][j] = '0' + matrix[k][j]
                    for k in range(n):
                        if matrix[i][k] != '0': matrix[i][k] = '0' + matrix[i][k]
                        
        for i in range(m):
            for j in range(n):
                if matrix[i][j][0] == '0': matrix[i][j] = 0
                else: matrix[i][j] = int(matrix[i][j])


    def setZeroes(self, matrix):
        """
        Using first row and first column to represent states.

        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0: return
        n = len(matrix[0])
        if n == 0: return
        first_row_zero = first_column_zero = False

        for i in range(m):
            if matrix[i][0] == 0:
                first_column_zero = True

        for i in range(n):
            if matrix[0][i] == 0:
                first_row_zero = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        if first_row_zero:
            for i in range(0, n):
                matrix[0][i] = 0
        if first_column_zero:
            for i in range(0, m):
                matrix[i][0] = 0



def print_matrix(matrix):
    for line in matrix:
        print(line)
    print('-'*20)

matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
print_matrix(matrix)

a = Solution()
a.setZeroes(matrix)
print_matrix(matrix)




















