class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Basic dynamic programming
        
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        # word_lst = list(wordDict)
        f = [[] for i in range(len(s)+1)]
        
        for i in range(len(s)):
            if f[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        f[i+len(word)].extend(map(lambda x: x+' '+word, f[i]))
            elif i == 0:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        f[len(word)].append(word)
        
        for i, val in enumerate(f):
            print('f[{0}]: {1}'.format(i, val))

        return f[len(s)]

        
    def wordBreak(self, s, wordDict):
        """
        Dynamic programming with subsequent dealing.

        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        word_lst = list(wordDict)
        f = [[] for i in range(len(s)+1)]

        for i in range(len(s)):        
            if i == 0 or f[i]:
                for index, word in enumerate(word_lst):
                    if word == s[i:i+len(word)]:
                        f[i+len(word)].append(index)

        res_lst = []
        def dfs(index, sentence):
            '''Backtrack to construct possible sentences'''
            if index == 0:
                res_lst.append(sentence)
                return
            elif index < 0:
                return

            for i in f[index]:
                if not sentence:
                    dfs(index-len(word_lst[i]), word_lst[i])
                else:
                    dfs(index-len(word_lst[i]), word_lst[i]+' '+sentence)

        dfs(len(s), '')
        return res_lst



a = Solution()

s = "catsanddog"
dct = ["cat", "cats", "and", "sand", "dog"]

print(a.wordBreak(s, dct))