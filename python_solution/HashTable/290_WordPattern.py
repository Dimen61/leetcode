class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_map = dict()
        word_map = dict()
        word_lst = str.split()
        
        if len(word_lst) != len(pattern):
            return False
        
        for index, word in enumerate(word_lst):
            if pattern[index] not in pattern_map and word not in word_map:
                pattern_map[pattern[index]] = word
                word_map[word] = pattern[index]
            elif pattern_map.get(pattern[index]) == word and word_map.get(word) == pattern[index]:
                continue
            else:
                return False
            
        return True
            
        
a = Solution()
print(a.wordPattern("abba", "dog dog dog dog"))