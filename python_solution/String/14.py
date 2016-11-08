class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        if not strs: return res # Empty list strs

        for i in range(len(strs[0])):
            char = strs[0][i]
            flag = True
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    flag = False
                    break
            if not flag: 
                return res
            else:
                res += char
        return res


a = Solution()
print(a.longestCommonPrefix(['abc', 'ab']))
print(a.longestCommonPrefix([]))