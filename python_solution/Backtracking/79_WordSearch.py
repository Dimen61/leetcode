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

        def dfs(index, x, y, path):
            """
            if word[index:] could be constructed, return True, otherwise
            return False.

            :type index: int
            :type x: int
            :type y: int
            :rtype: bool
            """
            if index >= length-1:
                return True
            
            xx = [1, -1, 0,  0]
            yy = [0,  0, 1, -1]
            for i in range(4):
                new_x = xx[i] + x
                new_y = yy[i] + y
                if 0 <= new_x < n and 0 <= new_y < m and board[new_y][new_x] == word[index+1]:
                    tmp = board[new_y][new_x]
                    board[new_y][new_x] = '#'
                    if dfs(index+1, new_x, new_y, path+[(new_x, new_y)]): return True
                    board[new_y][new_x] = tmp
            return False
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]: 
                    board[i][j] = '#'
                    if dfs(0, j, i, [(j, i)]): return True
                    board[i][j] = word[0]
        return False
                    

a = Solution()
# print(a.exist([list("ABCE"),list("SFCS"),list("ADEE")], "ABCCED"))
print(a.exist([list('aa')], 'aaa'))
# print(a.exist([list("ABCE"),list("SFCS"),list("ADEE")], "ABCCED"))

# ABCE
# SFCS
# ADEE

# ABCCED





