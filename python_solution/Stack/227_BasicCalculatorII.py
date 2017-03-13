# One stack
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sign = '+'
        num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if (i == len(s) - 1) or s[i] in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    num0 = stack.pop()
                    val = num0 // num
                    if val < 0 and num0 % num > 0:
                        val += 1
                    stack.append(val)
                    
                sign = s[i]
                num = 0
        return sum(stack)


# Two stack
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_stack = []
        opt_stack = []
        num = 0
        for c in s:
            if c == ' ': continue
            if c.isdigit():
                num = num*10 + ord(c) - ord('0')
            else:
                if c in '+-':
                    num_stack.append(num)
                    num = 0
                    opt_stack.append(c)
                elif c in '*/':
                    num_stack.append(num)
                    num = 0
                    while opt_stack and opt_stack[-1] in '*/':
                        num2 = num_stack.pop()
                        num1 = num_stack.pop()
                        opt = opt_stack.pop()
                        if opt == '*':
                            num_stack.append(num1 * num2)
                        elif opt == '/':
                            num_stack.append(num1 // num2)
                    opt_stack.append(c)
        num_stack.append(num)

        total = 0
        while opt_stack:
            opt = opt_stack.pop()
            if opt == '*':
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(num1 * num2)
            elif opt == '/':
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(num1 // num2)
            elif opt == '-':
                total -= num_stack.pop()
            elif opt == '+':
                total += num_stack.pop()

        total += num_stack.pop()
        return total











