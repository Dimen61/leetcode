class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        
        def is_attacked(x1, y1, x2, y2):
            """
            :type x1: int
            :type y1: int
            :type x2: int
            :type y2: int
            :rtype: void
            """
            if x1 == x2 or y1 == y2:
                return True
            elif abs(x1 - x2) == abs(y1 - y2):
                return True
            else:
                return False
            
        
        def is_placing_ok(x, y, board):
            """
            :type x: int
            :type y: int
            :type board: List[str]
            :rtype: void
            """
            m = len(board)
            for i in range(m):
                for j in range(m):
                    try:
                        if board[i][j] == 'Q' and is_attacked(j, i, x, y):
                            return False
                    except Exception as e:
                        print(e)
                        print('i: {0}; j: {1}; m: {2}'.format(i, j, m))
            return True
        
        def dfs_search(index, board):
            """
            :type index: int
            :type board: int
            :rtype: void
            """
            if index >= n:
                result.append([''.join(board[i]) for i in range(len(board))])
                return
            
            m = len(board)
            for i in range(m):
                if board[index][i] == '.' and is_placing_ok(i, index, board):
                    board[index][i] = 'Q'
                    dfs_search(index+1, board)
                    board[index][i] = '.'
                    
        board = [['.']*n for j in range(n)]
        dfs_search(0, board)
        return result  
            
def print_matrix(matrix):
    """
    :type matrix: List[str]
    :rtype: void
    """
    for line in matrix:
        print(line)
    print('-'*20)

a = Solution()
for matrix in a.solveNQueens(4):
    print_matrix(matrix)