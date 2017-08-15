# Dictionary
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            if count[c] == 0:
                return c
            else:
                count[c] -= 1


# Difference
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        total = 0
        for c in t:
            total += ord(c)
        for c in s:
            total -= ord(c)
        return chr(total)

# XOR
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for c in (s+t):
            res ^= ord(c)
        return chr(res)


        
if __name__ == '__main__':
    s = Solution()
    print(s.findTheDifference('abcd', 'abcde'))