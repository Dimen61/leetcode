class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
        
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        
        len_n = len(needle)
        for i in range(len(haystack) - len_n + 1):
            if needle == haystack[i:i+len_n]:
                return i

        return -1