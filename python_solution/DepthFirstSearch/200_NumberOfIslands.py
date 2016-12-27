class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        
        m, n = len(grid), len(grid[0])
        
        island_num = 0
        grid_visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        
        def dfs(y, x):
            """
            :type y: int
            :type x: int
            """
            grid_visited[y][x] = True
            arounds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x_step, y_step in arounds:
                new_x = x + x_step
                new_y = y + y_step
                if 0 <= new_x < n and 0 <= new_y < m:
                    if not grid_visited[new_y][new_x] and grid[new_y][new_x] == '1':
                        dfs(new_y, new_x)
                    
        for i in range(m):
            for j in range(n):
                if not grid_visited[i][j] and grid[i][j] == '1':
                    island_num += 1
                    dfs(i, j)
                    
        return island_num