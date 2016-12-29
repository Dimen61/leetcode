class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        Using memorized search.
        
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        
        m, n = len(matrix), len(matrix[0])
        f = [[False for i in range(n)] for i in range(m)]
        
        def m_search(x, y):
            if f[y][x]: return f[y][x]
        
            f[y][x] = 1
            deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for delta_x, delta_y in deltas:
                new_x = x + delta_x
                new_y = y + delta_y
                if 0 <= new_x < n and 0 <= new_y < m and matrix[new_y][new_x] > matrix[y][x]:
                    f[y][x] = max(f[y][x], m_search(new_x, new_y)+1)
                    
            return f[y][x]
            
        longest = 0
        for y in range(m):
            for x in range(n):
                longest = max(longest, m_search(x, y))
        
        return longest
        
        
a = Solution()
print(a.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))


