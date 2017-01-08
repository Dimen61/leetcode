class Solution(object):
    def findSubstring(self, s, words):
        """
        DFS

        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        start_indexs = set()

        def dfs(start, index, current_words):
            if index <= len(s) and not current_words:
                start_indexs.add(start)
                return 
            elif index >= len(s):
                return

            for word in current_words:
                if s[index:index+len(word)] == word:
                    next_words = current_words[:]
                    next_words.remove(word)
                    dfs(start, index+len(word), next_words)

        for i in range(len(s)-len(''.join(words))+1):
            dfs(i, i, words[:])

        return list(start_indexs)

import collections
class Solution2(object):
    def findSubstring(self, s, words):
        """
        An intuitive approach.

        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(s)
        w_len = len(words[0])
        f = [False for i in range(n)]
        words_dict = collections.defaultdict(int)
        for word in words:
            words_dict[word] += 1

        res_lst = []
        for i in range(n):
            ok = True
            tmp_words_dict = collections.defaultdict(int)
            for j in range(len(words)):
                word = s[i+j*w_len : i+(j+1)*w_len]
                if word not in words_dict: continue
                tmp_words_dict[word] += 1
            for word in words_dict:
                if words_dict[word] != tmp_words_dict[word]:
                    ok = False
                    break
            if ok:
                res_lst.append(i)

        return res_lst


class Solution3(object):
    def findSubstring(self, s, words):
        """
        Use the idea of two points that one is faster and
        another is slower.

        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(s)
        w_len = len(words[0])
        word_dict = collections.defaultdict(int)
        for word in words:
            word_dict[word] += 1
        res = []

        for i in range(w_len):
            word_count = collections.defaultdict(int)
            count = 0
            left, right = i, i+w_len

            print('i:', i)

            while right <= len(s):

                # if left == 8:
                #     print('right: {0}'.format(right))

                # print('left: {0}; right: {1}'.format(left, right))

                word = s[right-w_len:right]
                if word in word_dict:
                    word_count[word] += 1
                    if word_count[word] <= word_dict[word]:
                        count += 1
                    else:
                        while left < right:
                            delete_word = s[left:left+w_len]
                            word_count[delete_word] -= 1
                            left += w_len
                            if word_count[delete_word] < word_dict[delete_word]:
                                count -= 1
                            if word_count[word] == word_dict[word]: break
                            # print('left: {0}'.format(left))


                    if count == len(words):
                        res.append(left)
                        delete_word = s[left:left+w_len]
                        word_count[delete_word] -= 1
                        count -= 1
                        left += w_len
                else:
                    left = right
                    word_count.clear()
                    count = 0

                right += w_len

        return res


a = Solution3()
#                      012345678901234567
print(a.findSubstring("barfoothefoobarman", ["foo", "bar"]))

#                      012345678
# print(a.findSubstring("wordgoodgoodgoodbestword",
#                       ["word","good","best","good"]))












