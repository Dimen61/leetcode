class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        num = 0
        sign = 1
        sign_stack = [1]

        for c in s:
            if c == ' ':
                pass
            elif c in '+-':
                total += sign * num
                num = 0
                sign = sign_stack[-1] * (1 if c == '+' else -1)
            elif c == '(':
                sign_stack.append(sign)
            elif c == ')':
                sign_stack.pop()
            elif c.isdigit():
                num = num * 10 + int(c)
        total += sign * num
        return total


a = Solution()
print(a.calculate("   (  3 ) "))
# print(a.calculate("5   "))
# print(a.calculate('1'))
# print(a.calculate('(1)'))
