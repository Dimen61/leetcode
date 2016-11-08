class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.total_num = 0
        
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
            elif abs(x1-x2) == abs(y1-y2):
                return True
            else:
                return False
        
        def is_pos_ok(x, y, board):
            """
            :type x: int
            :type y: int
            :type board: List[str]
            :rtype: void
            """
            m = len(board)
            for i in range(m):
                for j in range(m):
                    if board[i][j] == 'Q' and is_attacked(j, i, x, y):
                        return False
            return True
        
        def dfs_search(index, board):
            """
            :type index: int
            :type board: List[str]
            :rtype void
            """
            if index >= n:
                self.total_num += 1
                return
            
            for i in range(n):
                if is_pos_ok(i, index, board):
                    board[index][i] = 'Q'
                    dfs_search(index+1, board)
                    board[index][i] = '.'
                    
        board = [['.']*n for i in range(n)]
        dfs_search(0, board)
        return self.total_num
        