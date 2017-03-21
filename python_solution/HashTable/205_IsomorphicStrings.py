# Use a hash table
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(s):
            return False
        
        s_map = dict()
        mapped_char = set()
        
        for i in range(len(s)):
            if s[i] in s_map:
                if t[i] != s_map[s[i]]:
                    return False
            else:
                if t[i] in mapped_char:
                    return False
                else:
                    s_map[s[i]] = t[i]
                    mapped_char.add(t[i])
                    
        return True
                    
# Pythonic
class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


# Map s and t to the index
# It could be implemented concisely
class Solution3(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = [-1] * 256
        t_map = [-1] * 256

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s_map[ord(s[i])] != t_map[ord(t[i])]:
                return False
            s_map[ord(s[i])], t_map[ord(t[i])] = i, i

        return True


















