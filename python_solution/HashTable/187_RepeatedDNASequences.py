import collections
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sequences_num = collections.defaultdict(int)
        ans = []
        for i in range(len(s)-9):
            sequences_num[s[i:i+10]] += 1
            if sequences_num[s[i:i+10]] > 1:
                ans.append(s[i:i+10])
        return ans
                
        