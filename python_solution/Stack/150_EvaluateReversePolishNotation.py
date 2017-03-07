class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        num_stack = []
        for token in tokens:
            if token == '+':
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                num_stack.append(num1 + num2)
            elif token == '-':
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                num_stack.append(num2 - num1)
            elif token == '*':
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                num_stack.append(num2 * num1)
            elif token == '/':
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                num_stack.append(abs(num2) // num1 * (-1 if num1 * num2 < 0 else 1))
                num_stack.append(int(num2 / num1))
              else:
                num_stack.append(int(token))

            print(num_stack)
        
        assert len(num_stack) == 1
        return num_stack[0]
        

a = Solution()
# print(a.evalRPN(["4", "13", "5", "/", "+"]))
print(a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
