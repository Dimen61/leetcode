class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def word2int(word):
            """Convert word to integer which binary form could present the word"""
            res_int = 0
            for c in word:
                res_int |= 1 << (ord(c) - ord('a'))
            return res_int
          
        max_product = 0    
        ints = list(map(word2int, words))
        for i in range(len(ints)):
            for j in range(i+1, len(ints)):
                if ints[i] & ints[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
                    
        return max_product