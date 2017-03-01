class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.graph = [collections.defaultdict(str)]
        self.end_nodes = set()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = None
        for index, c in enumerate(word):
            if index == 0:
                node = 0
            if c not in self.graph[node]:
                self.graph[node][c] = len(self.graph)
                self.graph.append(collections.defaultdict(str))
            node = self.graph[node][c]
        self.end_nodes.add(node)
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = 0
        for c in word:
            if c not in self.graph[node]:
                return False
            node = self.graph[node][c]
        return node in self.end_nodes

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = 0
        for c in prefix:
            if c not in self.graph[node]:
                return False
            node = self.graph[node][c]
        return True

# Another more intuitive implement.
class TrieNode(object):
    
    def __init__(self):
        self.children = dict()
        self.is_word = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)