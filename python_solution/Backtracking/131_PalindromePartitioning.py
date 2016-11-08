class Solution(object):
    def is_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s == s[::-1]
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        partitions = []
        length = len(s)
        def search(rest_s, collect):
            """
            :type rest_s: str
            :type collect: List[str]
            :rtype: void
            """
            if not rest_s:
                partitions.append(collect)
                return
            for i in range(len(rest_s)):
                if self.is_palindrome(rest_s[:i+1]):
                    search(rest_s[i+1:], collect + [rest_s[:i+1]])
            
        search(s, [])
        return partitions
        