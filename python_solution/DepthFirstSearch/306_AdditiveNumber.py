class Solution(object):
    def isAdditiveNumber(self, num):
        """
        DFS, slow without using the definition of additive sequences
        enough.

        :type num: str
        :rtype: bool
        """
        self.flag = False
        self.n = len(num)
        def dfs(num, prev, prev_v):
            if self.flag: return True
            if not num and prev != None and prev_v != None and len(str(prev)+str(prev_v)) < self.n:
                self.flag = True
                return True
                
            for i in range(1, len(num)+1):
                cur_str, cur_val = num[:i], int(num[:i])
                rest_str = num[i:]
                if len(cur_str) > 1 and cur_str[0] == '0':
                    continue
                if prev is None and prev_v is None: # 1st number
                    if dfs(rest_str, cur_val, None):
                        return True
                elif prev_v is None:            # 2nd number
                    if dfs(rest_str, cur_val, prev):
                        return True
                else:
                    if cur_val == prev+prev_v and dfs(rest_str, cur_val, prev):
                        return True
            return False
        return dfs(num, None, None)

class Solution2(object):
    def isAdditiveNumber(self, num):
        """
        Iteration

        :type num: str
        :rtype: bool
        """
        n = len(num)

        def is_valid(s):
            return False if len(s) > 1 and s[0] == '0' else True

        count = 0
        for i in range(1, n//2+1):
            for j in range(1, n-i+1):  # The second number could be less than the first number
                first, second, rest = num[:i], num[i:i+j], num[i+j:]
                if is_valid(first) and is_valid(second):
                    while rest:
                        third = str(int(first) + int(second))
                        if is_valid(rest) and int(third) == int(rest):
                            return True
                        if rest.startswith(third):
                            first, second, rest = second, third, rest[len(third):]
                        else:
                            break

        return False

a = Solution2()
# print(a.isAdditiveNumber('111'))
# print(a.isAdditiveNumber('101'))
# print(a.isAdditiveNumber("0235813"))
print(a.isAdditiveNumber("12012122436"))

