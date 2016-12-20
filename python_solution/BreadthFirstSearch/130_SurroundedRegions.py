class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return 
    
        m = len(board)
        n = len(board[0])
        visited = [[False for i in range(n)] for j in range(m)]
        tmp_board = [list(line) for line in board]

        xx = [1, -1, 0, 0]
        yy = [0, 0, -1, 1]
            
        def dfs_one_part(x, y):
            """
            Judge one region 0 are surrounded by X or not.
            
            :type x: int
            :type y: int
            :rtype: void
            """
            surrounded = True
            nodes = []
            queue = [(x, y)]
            
            while queue:
                node = queue.pop(0)
                nodes.append(node)
                visited[node[1]][node[0]] = True
                for i in range(4):
                    new_x = xx[i] + node[0]
                    new_y = yy[i] + node[1]
                    if 0 <= new_x < n and 0 <= new_y < m and board[new_y][new_x] == 'O' and not visited[new_y][new_x]:
                        queue.append((new_x, new_y))
                    elif new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                        surrounded = False
                        
            if surrounded:
                for node in nodes:
                    tmp_board[node[1]][node[0]] = 'X'
                #     print(node)
                # print('x: {0}; y: {1}'.format(x, y))
                    
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == 'O':
                    dfs_one_part(j, i)

        # board = [''.join(line) for line in board]        
        for i in range(len(board)):
            board[i] = ''.join(tmp_board[i])

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return 
    
        m = len(board)
        n = len(board[0])
        tmp_board = [list(line) for line in board]

            
        def bfs_one_part(x, y):
            """
            Judge one region 0 are surrounded by X or not.
            
            :type x: int
            :type y: int
            :rtype: void
            """
            from collections import deque

            xx = [1, -1, 0, 0]
            yy = [0, 0, -1, 1]
        
            queue = deque([(x, y)])
            while queue:
                node = queue.popleft()

                # print('x:{0}; y:{1};'.format(node[0], node[1]))

                tmp_board[node[1]][node[0]] = 'B'
                for i in range(4):
                    new_x = xx[i] + node[0]
                    new_y = yy[i] + node[1]
                    if 0 <= new_x < n and 0 <= new_y < m and tmp_board[new_y][new_x] == 'O':
                        queue.append((new_x, new_y))
                    
                            
        for i in range(m):
            if tmp_board[i][0] == 'O': bfs_one_part(0, i)
            if tmp_board[i][n-1] == 'O': bfs_one_part(n-1, i)
        for i in range(n):
            if tmp_board[0][i] == 'O': bfs_one_part(i, 0)
            if tmp_board[m-1][i] == 'O': bfs_one_part(i, m-1)
            
        # for line in tmp_board:
        #     print(line)

        for i in range(m):
            for j in range(n):
                if tmp_board[i][j] == 'B':
                    tmp_board[i][j] = 'O'
                elif tmp_board[i][j] == 'O':
                    tmp_board[i][j] = 'X'
                    
        for i in range(len(board)):
            board[i] = ''.join(tmp_board[i])


    def solve(self, board):
        if not any(board): return

        m, n = len(board), len(board[0])
        save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        tmp_board = [list(line) for line in board]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and tmp_board[i][j] == 'O':
                tmp_board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        for row in tmp_board:
            for i, c in enumerate(row):
                row[i] = 'XO'[c == 'S']

        for i in range(m):
            board[i] = ''.join(tmp_board[i])


a = Solution()
board = ["XXXX","XOOX","XXOX","XOXX"]
for line in board:
    print(line)
a.solve(board)
print('-'*30)
for line in board:
    print(line)
