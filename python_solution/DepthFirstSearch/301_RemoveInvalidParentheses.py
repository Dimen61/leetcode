import collections
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        visited = set()
        level = [s]
        
        def is_valid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        def count_valid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
            return abs(count)
        
        res = []
        found = False
        while not found and level:
            next_level = []
            for node in level:
                if is_valid(node):
                    if node not in res:
                        res.append(node)    
                    found = True
                else:
                    count_0 = count_valid(node)
                    for i in range(len(node)):
                        if node[i] in '()':
                            new_node = node[:i] + node[i+1:] 
                            count_1 = count_valid(new_node)
                            if new_node not in visited and count_1 < count_0:
                                visited.add(new_node)
                                next_level.append(new_node)

            level = next_level
        
        return res
            

class Solution2(object):
    def removeInvalidParentheses(self, s):
        """
        DFS. 
        The main idea is 'mis_count'. The least number of parentheses for removing
        is certain. It's easy to understand the code if get 'mis_count'.

        :type s: str
        :rtype: List[str]
        """
        visited = set()
        res_lst = []

        def mis_count(s):
            '''
            The least number to remove for getting matched
            parentheses.
            '''
            mis_l = mis_r = 0
            for c in s:
                if c == '(':
                    mis_l += 1
                elif c == ')':
                    if mis_l > 0:
                        mis_l -= 1
                    else:
                        mis_r += 1
            return mis_l + mis_r

        def dfs(s):
            count = mis_count(s)
            if count == 0:
                res_lst.append(s)
                return

            for i in range(len(s)):
                if s[i] in '()':
                    new_s = s[:i] + s[i+1:]
                    if new_s not in visited and mis_count(new_s) < count:
                        visited.add(new_s)
                        dfs(new_s)

        visited.add(s)
        dfs(s)
        return res_lst



        
a = Solution2()

print(a.removeInvalidParentheses("()())()"))