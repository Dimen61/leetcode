class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m = n = 9
        
        def check_row(row_num):
            tmp_set = set()
            for i in range(n):
                if board[row_num][i] not in '.0123456789':
                    return False
                elif board[row_num][i] not in tmp_set:
                    tmp_set.add(board[row_num][i])
                elif board[row_num][i] != '.': 
                    return False
            return True
            
        def check_column(column_num):
            tmp_set = set()
            for i in range(m):
                if board[i][column_num] not in '.0123456789':
                    return False
                elif board[i][column_num] not in tmp_set:
                    tmp_set.add(board[i][column_num])
                elif board[i][column_num] != '.':
                    return False
            return True
            
        def check_block(x, y):
            deltas = [(-1, -1), (0, -1), (1, -1), 
                     (-1, 0), (0, 0), (1, 0),
                     (-1, 1), (0, 1), (1, 1)]
            tmp_set = set()
            for x_d, y_d in deltas:
                new_x = x + x_d
                new_y = y + y_d
                if board[new_y][new_x] not in '.0123456789':
                    return False
                elif board[new_y][new_x] not in tmp_set:
                    tmp_set.add(board[new_y][new_x])
                elif board[new_y][new_x] != '.':
                    return False
            return True
            
        nodes = [(x, y) for x in range(1, 8, 3) for y in range(1, 8, 3)]
        for i in range(9):
            if not check_row(i): 
                return False
            if not check_column(i): 
                return False
            if not check_block(*nodes[i]): 
                return False        
        return True
            

a = Solution()
print(a.isValidSudoku([".87654321",
                       "2........",
                       "3........",
                       "4........",
                       "5........",
                       "6........",
                       "7........","8........","9........"]))