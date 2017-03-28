class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''

        char_num = {}
        for c in s:
            char_num[c] = char_num.get(c, 0) + 1

        small_index = -1
        small_char = None
        for i in range(len(s)):
            char_num[s[i]] -= 1
            if not small_char or small_char > s[i]:
                small_char = s[i]
                small_index = i
            if char_num[s[i]] == 0:
                return small_char + self.removeDuplicateLetters(s[small_index+1:].replace(small_char, ''))
                
        
                
