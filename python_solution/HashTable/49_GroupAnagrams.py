import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_dict = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            anagrams_dict[key].append(s)
        return list(anagrams_dict.values())
        
            
        