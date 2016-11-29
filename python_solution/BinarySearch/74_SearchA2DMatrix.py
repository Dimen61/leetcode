class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Use binary search, find the line where target in firstly.
        Then use binary search again to find target in that line.
        
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Search the line firstly
        left, right = 0, len(matrix)-1
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid
        
        line_num = min(left, len(matrix)-1)
        # Search the target in the line
        left, right = 0, len(matrix[0]) - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[line_num][mid] < target:
                left = mid + 1
            else:
                right = mid
                
        return matrix[line_num][left] == target