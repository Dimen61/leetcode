class Solution1(object):
    def addOperators(self, num, target):
        """
        Implement DFS with eval expression(time limited)

        :type num: str
        :type target: int
        :rtype: List[str]
        """
        exp_lst = []
        n = len(num)
        
        def is_valid(exp):
            if len(exp) > 1 and exp[0] == '0': return False
            
            prev = '#'
            for i, c in enumerate(exp):
                if (prev in '*-+' or prev == '#') and c == '0' and i < len(exp)-1 and exp[i+1] in '0123456789':
                    return False
                prev = c
            return True
        
        def dfs(seqs):
            # Add candidate expressions
            if len(seqs) >= n-1:
                tmp_lst = []
                for i in range(len(num)):
                    if i == 0:
                        tmp_lst.append(num[i])
                    else:
                        tmp_lst.extend([seqs[i-1], num[i]])
                exp = ''.join(tmp_lst)
                res = eval(exp)
                if is_valid(exp) and res == target:
                    exp_lst.append(exp)
                return 
            
            for c in ('', '+', '-', '*'):
                dfs(seqs+[c])
                
        dfs([])
        return exp_lst
            
        
class Solution2(object):
    def addOperators(self, num, target):
        """
        Implement DFS without eval expression.
        The trick here is regarding 'prev' as stack and getting
        value in this way if operator now is '*':
        value - prev + prev*cur_val

        :type num: str
        :type target: int
        :rtype: List[str]
        """
        exp_lst = []
        n = len(num)

        def dfs(num, exp, prev, value):
            if not num:
                if value == target:
                    exp_lst.append(exp)
                return

            for i in range(1, len(num)+1):
                cur_str, cur_val = num[:i], int(num[:i])
                if len(cur_str) > 1 and cur_str[0] == '0':
                    continue

                if len(num) == n:
                    dfs(num[i:], cur_str, cur_val, cur_val)
                else:
                    dfs(num[i:], exp+'+'+cur_str, cur_val, value+cur_val)
                    dfs(num[i:], exp+'-'+cur_str, -cur_val, value-cur_val)
                    dfs(num[i:], exp+'*'+cur_str, prev*cur_val, value-prev+prev*cur_val)


        dfs(num, '', '', 0)
        return exp_lst


a = Solution2()

print(a.addOperators('123', 6))
print(a.addOperators('232', 8))









