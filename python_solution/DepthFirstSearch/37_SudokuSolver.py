import itertools
class Solution(object):
    def solveSudoku(self, board):
        """
        One DFS implement, failed.

        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = m = 9

        # def permutation(lst):
        #     '''
        #     :type lst: List[(int, int)]
        #     :rtyp: List[List[(int, int)]]
        #     '''
        #     res = []
        #     visited = [False for i in range(len(lst))]

        #     def dfs(index, seq):
        #         if index >= len(lst):
        #             res.append(seq)
        #             return
        #         for x in lst:
        #             if not visited[x]:
        #                 visited[x] = True
        #                 dfs(index+1, seq+[x])
        #                 visited[x] = False

        #     dfs(0, [])

        #     return res


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

        def check_block(i):
            # nodes = [(1, 1), (4, 1), (9, 1),
            #          (1, 4), (4, 4), (9, 4),
            #          (1, 9), (4, 9), (9, 9)]
            nodes = [(x, y) for x in range(1, 8, 3) for y in range(1, 8, 3)]

            x, y = nodes[i]
            deltas = [(-1, -1), (0, -1), (1, -1), 
                     (-1, 0), (0, 0), (1, 0),
                     (-1, 1), (0, 1), (1, 1)]
            total = 0
            for x_d, y_d in deltas:
                new_x = x + x_d
                new_y = y + y_d
                total += int(board[new_y][new_x])
            return total == 45

        nodes = [(x, y) for x in range(1, 8, 3) for y in range(1, 8, 3)]
        nodes.append((-1, -1))
        deltas = [(-1, -1), (0, -1), (1, -1), 
         (-1, 0), (0, 0), (1, 0),
         (-1, 1), (0, 1), (1, 1)]


        self.found = False
        def dfs(block_index):
            if self.found: return
            if block_index >= 9:
                self.found = True
                return 

            x, y = nodes[block_index]
            new_nodes = []
            used_num = set()
            for x_d, y_d in deltas:
                new_x = x + x_d
                new_y = y + y_d
                if board[new_y][new_x] == '.':
                    new_nodes.append((new_x, new_y))
                else:
                    print('board[{0}][{1}]: {2}'.format(new_y, new_x, board[new_y][new_x]))
                    used_num.add(board[new_y][new_x])

            left_num = set('123456789') - used_num

            # print('used_num:', used_num)

            for nums in itertools.permutations(left_num):

                flag = True
                for i in range(len(new_nodes)):
                    x, y = new_nodes[i]
                    board[y][x] = nums[i]
                    if not check_row(y) or not check_column(x):
                        flag = False
                        break

                if flag and check_block(block_index):
                    dfs(block_index+1)
                if self.found: return
                for i in range(len(new_nodes)):
                    x, y = new_nodes[i]
                    board[y][x] = '.'

        dfs(0)


class Solution2(object):
    def solveSudoku(self, board):
        """
        One DFS implement. The idea worth attention is how judge a
        value is valid in row, col and panel position.

        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row_hash = [[0]*9 for i in range(9)]
        col_hash = [[0]*9 for i in range(9)]
        panel_hash = [[0]*9 for i in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    val = int(val) - 1
                    row_hash[i][val] = 1
                    col_hash[j][val] = 1
                    panel_index = i // 3 * 3 + j // 3
                    panel_hash[panel_index][val] = 1

        def dfs(index):
            if index >= 81:
                return True

            row, col = index // 9,  index % 9
            panel_index = row // 3 * 3 + col // 3
            if board[row][col] == '.':
                for c in range(9):
                    if not row_hash[row][c] and not col_hash[col][c] and \
                       not panel_hash[panel_index][c]:
                        row_hash[row][c] = col_hash[col][c] = 1
                        panel_hash[panel_index][c] = 1
                        board[row][col] = str(c+1)
                        if dfs(index + 1):
                           return True
                        board[row][col] = '.'
                        row_hash[row][c] = col_hash[col][c] = 0
                        panel_hash[panel_index][c] = 0

                return False 
                    
            else:
                return dfs(index+1)

        dfs(0)



a = Solution2()
board = [list("..9748..."),
         list("7........"),
         list(".2.1.9..."),
         list("..7...24."),
         list(".64.1.59."),
         list(".98...3.."),
         list("...8.3.2."),
         list("........6"),
         list("...2759..")]
a.solveSudoku(board)
for line in board:
    print(line)










