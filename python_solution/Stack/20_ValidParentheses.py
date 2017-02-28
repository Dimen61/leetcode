class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        f = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            elif stack and f[c] == stack[-1]:
                stack.pop()
            else: 
                return False
        return len(stack) == 0
                