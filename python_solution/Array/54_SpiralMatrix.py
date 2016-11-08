class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        
        m = len(matrix)
        n = len(matrix[0])
        if sum([1 for items in matrix if not items]) == m:
            return []

        res_lst = []
        if m == 1 or n == 1:
            for items in matrix:
                res_lst.extend(items)
            return res_lst
        
        res_lst.extend(matrix[0])
        for i in range(1, m-1):
            res_lst.append(matrix[i][-1])
        res_lst.extend(matrix[-1][::-1])
        for i in range(1, m-1)[::-1]:
            res_lst.append(matrix[i][0])
        
        sub_matrix = []
        for i in range(1, m-1):
            sub_matrix.append(matrix[i][1:-1])

        res_lst.extend(self.spiralOrder(sub_matrix))
        return res_lst
        
        
a = Solution()
print(a.spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]))