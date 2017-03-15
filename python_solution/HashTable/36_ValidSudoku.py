class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check row
        for row in board:
            visited = set()   
            for c in row:
                if c == '.': continue
                elif c in visited:
                    return False
                else:
                    visited.add(c)
                
        
        # Check colmun
        for i in range(9):
            visited = set()
            for j in range(9):
                c = board[j][i]
                if c == '.': continue
                elif c in visited:
                    return False
                else:
                    visited.add(c)
                    
        # Check 9 blocks
        block_visited = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                block_index = (j // 3) + (i // 3) * 3
                c = board[i][j]
                if c == '.': continue
                elif c in block_visited[block_index]:
                    return False
                else:
                    block_visited[block_index].add(c)
                    
        return True
                