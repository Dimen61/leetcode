class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        for c in s:
            if c.lower() in 'aeiou':
                vowels.append(c)
        vowels.reverse()
        
        res = []
        index = 0
        for c in s:
            if c.lower() in 'aeiou':
                res.append(vowels[index])
                index += 1
            else:
                res.append(c)
                
        return ''.join(res)
        
# Two pointer
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            if s[left].lower() not in 'aeiou':
                left += 1
            elif s[right].lower() not in 'aeiou':
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
        return ''.join(s)