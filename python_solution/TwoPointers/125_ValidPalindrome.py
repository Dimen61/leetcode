import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        s = s.lower()
        
        while left < right:
            if s[left] not in (string.ascii_letters + string.digits):
                left += 1
            elif s[right] not in (string.ascii_letters + string.digits):
                right -= 1
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
                
        return True
        