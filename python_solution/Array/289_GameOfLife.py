class Solution(object):
    def liveAroundCellNum(self, i, j, board):
        """
        Return the live cell number around the position (i, j)
        in the board.
        """
        direct_x = [1, -1, -1,  0,  1, -1, 0, 1]
        direct_y = [0,  0, -1, -1, -1,  1, 1, 1]
        m = len(board)
        n = len(board[0])
        live_num = 0
        
        for k in range(8):
            x = direct_x[k] + j
            y = direct_y[k] + i
            if 0 <= x < n and 0 <= y < m and board[y][x] % 2 > 0 :
                live_num += 1

        return live_num
    

    # def liveAroundCellNum(self, i, j, board):
    #     """
    #     Return the live cell number around the position (i, j)
    #     in the board.
    #     """
    #     m = len(board)
    #     if m == 0: return
    #     n = len(board[0])
    #     if n == 0: return

    #     live_num = 0
    #     for direct_y in range(-1, 2):
    #         for direct_x in range(-1, 2):
    #             y = direct_y + i
    #             x = direct_x + j
    #             if 0 <= x < n and 0 <= y < m:
    #                 live_num += board[y][x]
    #     return live_num - board[i][j]

    def gameOfLife(self, board):
        """
                next_state current_state
        (01) represents (dead, live)
        (00) represents(dead, dead)
        (11) represents(live, live)
        (10) represents(live, dead)

        At the begin, any value in the board is either (01) or (00).
        (01) => (11) if 2 <= around_live_num <= 3
        (00) => (10) if around_live_num == 3

        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board) 
        if m == 0: return
        n = len(board[0])
        if n == 0: return

        for i in range(m):
            for j in range(n):
                live_num = self.liveAroundCellNum(i, j, board)

                if board[i][j] == 0 and live_num == 3:
                    board[i][j] = 2 # (00) => (10)
                elif board[i][j] == 1 and 2 <= live_num <= 3:
                    board[i][j] = 3 # (01) => (11)

        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] >> 1

def print_matrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void
    """
    for line in matrix:
        print(' '.join(map(str, line)))
    print('-'*30)

a = Solution()
# 1 1
# 1 0
board = [[1,1],[1,0]]
a.gameOfLife(board)
print('board:')
print(board)


# def generate_random_matrix(m, n):
#     """
#     :type m: int
#     :type n: int
#     :rtype: List[List[int]]
#     """
#     import random
#     matrix = []
#     for i in range(m):
#         line = []
#         for j in range(n):
#             line.append(random.randint(0, 1))
#         matrix.append(line)

#     return matrix

# def time_goes_by(num):
#     import time
#     # matrix = [[0, 0, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]]
#     matrix = generate_random_matrix(24, 30)
#     print_matrix(matrix)
#     a = Solution()
#     for i in range(num):
#         # time.sleep(1)
#         a.gameOfLife(matrix)
#         if i == 0:
#             print('After {0} generation:'.format(i+1))
#         else:
#             print('After {0} generations:'.format(i+1))
#         print_matrix(matrix)

# time_goes_by(1000)