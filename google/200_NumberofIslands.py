class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        num = 0
        # Use -1 to represent that the node is not visited before
        height = len(grid)
        width = len(grid[0])
        visited = [[False for i in range(width)] for i in range(height)]
        
        def dfs(x, y):
            move_x = [0, 0, -1, 1]
            move_y = [1, -1, 0, 0]
            
            for i in range(4):
                new_x = x + move_x[i]
                new_y = y + move_y[i]
                if 0 <= new_x < width and 0 <= new_y < height and not visited[new_y][new_x] and grid[new_y][new_x] == '1':
                    visited[new_y][new_x] = True
                    dfs(new_x, new_y)
                    
        # Count the num of island
        for i in range(height):
            for j in range(width):
                if not visited[i][j] and grid[i][j] == '1':
                    num += 1
                    visited[i][j] = True
                    dfs(j, i)
                    
        return num
                    
if __name__ == '__main__':
    s = Solution()
    print(s.numIslands(["11110","11010","11000","00000"]))
        
        