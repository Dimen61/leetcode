# Using stack to record ('s index.
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        stack = [-1]
        
        for index, c in enumerate(s):
            if c == '(':
                stack.append(index)
            elif c== ')':
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    cur_len = index - stack[-1]
                    max_len = max(max_len, cur_len)

        return max_len

# Use two pointer            
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = max_len = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                right += 1
            if left == right:
                max_len = max(max_len, 2*left)
            if right > left:
                left = right = 0

        left = right = 0
        for c in s[::-1]:
            if c == '(':
                left += 1
            elif c == ')':
                right += 1
            if left == right:
                max_len = max(max_len, 2*left)
            if left > right:
                left = right = 0

        return max_len

# Use dynamice programming
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        dp = [0] * len(s)
        for i, c in enumerate(s):
            if c == ')' and i > 0:
                if s[i-1] == '(':
                    dp[i] = 2
                    if i-2 >= 0:
                        dp[i] += dp[i-2]
                elif s[i-1] == ')':
                    if dp[i-1] > 0 and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                        dp[i] = 2 + dp[i-1]
                        if i-dp[i-1]-2 >= 0:
                            dp[i] += dp[i-dp[i-1]-2]
            if dp[i] > max_len:
                max_len = dp[i]
        return max_len

a = Solution()
# print(a.longestValidParentheses(')()())'))
# print(a.longestValidParentheses("()(())"))
print(a.longestValidParentheses("(()))())("))
#                                002460800
#                                012345678












