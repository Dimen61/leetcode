class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = [board[i][j], None]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                live_neigh_num = 0
                delta_x = [0, 0, 1, -1, 1, -1, 1, -1]
                delta_y = [1, -1, 0, 0, 1, -1, -1, 1]
                for k in range(8):
                    x = delta_x[k] + j
                    y = delta_y[k] + i
                    if 0 <= x < len(board[i]) and 0 <= y < len(board) and board[y][x][0] == 1:
                        live_neigh_num += 1
                        
                if board[i][j][0] == 1:
                    # Under-population
                    if live_neigh_num < 2:
                        board[i][j][1] = 0
                    elif live_neigh_num in (2, 3):
                        board[i][j][1] = 1
                    # Over-population
                    elif live_neigh_num > 3:
                        board[i][j][1] = 0
                else:
                    # Reproduction
                    if live_neigh_num == 3: 
                        board[i][j][1] = 1
                    else:
                        board[i][j][1] = 0
                        
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = board[i][j][1]
                    
                