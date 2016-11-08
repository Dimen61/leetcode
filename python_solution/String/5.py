class Solution(object):
    def longestPalindrome(self, s):
        """
        Algorithm: Expanding from the centre.

        :type s: str
        :rtype: str
        """
        if not s: return ''
        if len(s) == 1: return s

        max_palind = s[0]
        for i in range(len(s)):
            if (len(s) - i)*2 <= len(max_palind): break
            j = k = i
            while k < len(s)-1 and s[k] == s[k+1]: k += 1 # Skip duplicate char
            while k < len(s) and j >= 0 and s[k] == s[j]:
                k += 1
                j -= 1
            if k-j-1 > len(max_palind):
                max_palind = s[j+1:k]
        return max_palind


a_sol = Solution()
assert a_sol.longestPalindrome('ccc') == 'ccc'
assert a_sol.longestPalindrome('aba') == 'aba', 'bad'
