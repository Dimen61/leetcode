# Use memorized search
# Time out
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        seq = preorder.split(',')
        length = len(seq)
        f = [[None for j in range(length)] for i in range(length)]
        def is_valid(i, j):
            if f[i][j] != None:
                return f[i][j]
            
            if i > j: 
                f[i][j] = False
                return f[i][j]
            elif i == j: 
                f[i][j] = (seq[i] == '#')
                return f[i][j]
            elif j == i+1: 
                f[i][j] = False
                return f[i][j]
            else:
                if seq[i] == '#':
                    f[i][j] = False
                    return f[i][j]
                for k in range(i+1, j):
                    if is_valid(i+1, k) and is_valid(k+1, j):
                        f[i][j] = True
                        return f[i][j]
                f[i][j] = False
                return f[i][j]
        
        return is_valid(0, length-1)
        
# Use in-degree and out-degree
class Solution2(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        out_degree = 0
        in_degree = -1
        for c in preorder:
            in_degree += 1
            # This line should be here to check in-degree and out-degree in time
            if in_degree > out_degree: return False 
            if c != '#':
                out_degree += 2
            
        return in_degree == out_degree

# Use stack to eliminate '#'
class Solution3(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        stack = []
        
        def is_last_two_num_sign(stack):
            if len(stack) < 3: return False
            return stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#'
        
        for c in preorder:
            stack.append(c)
            while is_last_two_num_sign(stack):
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
                
        return stack == ['#']
        





