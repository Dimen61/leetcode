class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chr_to_index = dict()
        start = 0
        end = -1
        max_length = 0
        for index, char in enumerate(s):
            if char in chr_to_index and (start <= chr_to_index[char] <= end):
                start = chr_to_index[char] + 1
                end = index
            else:
                end = index
                if end-start+1 > max_length:
                    max_length = end-start+1
            chr_to_index[char] = index
                    
        return max_length
        
a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))
#                                 01234567