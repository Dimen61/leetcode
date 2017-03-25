class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        

import collections
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_num_map = collections.defaultdict(int)

        for c in s:
            char_num_map[c] += 1

        for c in t:
            if char_num_map[c] == 0:
                return False
            char_num_map[c] -= 1

        for c, num in char_num_map.items():
            if num > 0: return False

        return True

        