# Use recurrsion
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        
        char_num = dict()
        for c in s:
            char_num[c] = char_num.get(c, 0) + 1
        
        min_c = None
        pos = -1
        for index, c in enumerate(s):
            if min_c is None or min_c > c:
                pos = index
                min_c = c
            char_num[c] -= 1
            if char_num[c] == 0: break
        
        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ''))
        
        
# Use stack
class Solution2(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''

        char_num = dict()
        used = dict()
        for c in s:
            char_num[c] = char_num.get(c, 0) + 1
            used[c] = False

        stack = []
        for c in s:
            char_num[c] -= 1
            if used[c]: continue

            while stack and stack[-1] > c and char_num[stack[-1]] > 0:
                used[stack[-1]] = False
                stack.pop()

            stack.append(c)
            used[c] = True

        return ''.join(stack)

a = Solution()
print(a.removeDuplicateLetters('bcabc'))













