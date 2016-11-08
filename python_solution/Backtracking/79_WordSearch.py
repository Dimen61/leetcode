class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.result = False
        length = len(word)
        m = len(board)
        n = len(board[0])

        # print('m:', m)
        # print('n:', n)
        
        def dfs(index, x, y, path):
            """
            :type index: int
            :type x: int
            :type y: int
            :rtype void
            """
            if index >= length-1:
                self.result = True
                # print('path:', path)
                # print('index:', index)
                return
            
            # DEBUG
            # if index > 0: print('path:', path)

            xx = [1, -1, 0,  0]
            yy = [0,  0, 1, -1]
            for i in range(4):
                new_x = xx[i] + x
                new_y = yy[i] + y
                if 0 <= new_x < n and 0 <= new_y < m and board[new_y][new_x] == word[index+1]:
                    tmp = board[new_y][new_x]
                    board[new_y][new_x] = '#'

                    # print('-'*20)
                    # print('new_x:', new_x)
                    # print('new_y:', new_y)
                    # print('-'*20)

                    dfs(index+1, new_x, new_y, path+[(new_x, new_y)])
                    board[new_y][new_x] = tmp
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]: 
                    tmp = board[i][j]
                    board[i][j] = '#'
                    dfs(0, j, i, [(j, i)])
                    board[i][j] = tmp
        return self.result
                    

a = Solution()
# print(a.exist([list("ABCE"),list("SFCS"),list("ADEE")], "ABCCED"))
print(a.exist([list('aa')], 'aaa'))
# print(a.exist([list("ABCE"),list("SFCS"),list("ADEE")], "ABCCED"))

# ABCE
# SFCS
# ADEE

# ABCCED





