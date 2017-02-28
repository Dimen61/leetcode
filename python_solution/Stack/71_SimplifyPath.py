class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path: return path
            
        stack = []
        path = path.split('/')                    

        for item in path:
            if item == '..':
                if stack: stack.pop()
            elif item and item != '.':
                stack.append(item)

        return '/' + '/'.join(stack)
            
a = Solution()
print(a.simplifyPath('/...'))


