class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def search(left, right, parns):
            """
            :type left: int
            :type right: int
            :rtype: void
            """
            if left == right and left == n:
                result.append(parns)
                return
            elif right > left or left > n:
                return
            
            search(left+1, right, parns+'(')
            search(left, right+1, parns+')')
            
        search(0, 0, '')
        return result
            