from collections import defaultdict
class Solution1(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        Memorized search.

        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        self.shortest_len = 10000000
        self.shortest_seqs = []
        # visited_words = defaultdict(lambda: False)
        
        def is_transformable(s1, s2):
            assert len(s1) == len(s2)
            total = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    total += 1
            return total == 1
        
        def dfs(start, length, seq):
            if length > self.shortest_len: return
            if start == endWord:
                # print('seq:', seq, '; length:', length)
                if length < self.shortest_len:
                    self.shortest_len = length
                    self.shortest_seqs = [seq]
                elif length == self.shortest_len:
                    self.shortest_seqs.append(seq)
                return 

            # visited_words[start] = True
            for word in wordlist:
                # if not visited_words[word] and is_transformable(word, start):
                if word not in seq and is_transformable(word, start):
                    # visited_words[word] = True
                    dfs(word, length+1, seq+[word])
                    # visited_words[word] = False
        
        # visited_words[beginWord] = True
        dfs(beginWord, 1, [beginWord])
        
        return self.shortest_seqs


import string
class Solution2(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        BFS

        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        level = [(beginWord, [beginWord])]
        visited = set()
        shortest_seqs = []

        while level and endWord not in visited: 
            next_level = []
            for word, seq in level:
                for c in string.ascii_lowercase:
                    for i in range(len(word)):
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordlist and next_word not in visited:
                            next_level.append((next_word, seq+[next_word]))

            for word, _ in next_level:
                visited.add(word)
            level = next_level

        for word, seq in level:
            if word == endWord:
                shortest_seqs.append(seq)                

        return shortest_seqs

import collections
import string
class Solution3(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        Concise BFS (finally accepted solution.)

        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        parents = collections.defaultdict(set)
        level = {beginWord:None}

        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for c in string.ascii_lowercase:
                    for i in range(len(word)):
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordlist and next_word not in parents:
                            next_level[next_word].add(word)
            level = next_level
            parents.update(next_level)

        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p]+seq for seq in res for p in parents[seq[0]]]
        return res


class Solution4(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        SPFA

        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        def is_transformable(s1, s2):
            assert len(s1) == len(s2)
            total = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    total += 1
            return total == 1


        MAX = 10 ** 7
        # visited = []        
        # shortest = MAX
        # shortest_seqs = []

        dis = dict(zip(wordlist, [MAX for i in range(len(wordlist))]))
        dis[beginWord] = 0
        prev = dict()
        prev[beginWord] = None
        queue = [beginWord]

        while queue:
            word = queue.pop(0)
            for next_word in wordlist:
                if is_transformable(word, next_word):
                    if dis[word]+1 < dis[next_word]:
                        dis[next_word] = dis[word] + 1
                        prev[next_word] = set([word])
                        if next_word not in queue:
                            queue.append(next_word)
                    if dis[word]+1 == dis[next_word]:
                        prev[next_word].add(word)

        total_seqs = []

        def dfs(node, seq):
            if node not in prev:
                return
            elif not prev.get(node):
                total_seqs.append(seq)
                return

            for w in prev[node]:
                dfs(w, [w]+seq)

        dfs(endWord, [endWord])

        return total_seqs


        
a = Solution2()
print(a.findLadders('a', 'c', {'a', 'b', 'c'}))
# [["hot","dot","dog"],["hot","hog","dog"]]
print(a.findLadders("hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"]))
# "red"
# "tax"
# ["ted","tex","red","tax","tad","den","rex","pee"]

print(a.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))

print(a.findLadders("hot", "dog", ["hot","dog"]))

