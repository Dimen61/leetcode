class WordNode(object):
    
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordNode()
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = WordNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        
        def dfs(node, word):
            if not word:
                return node.is_word
                
            if word[0] != '.':
                return word[0] in node.children and dfs(node.children[word[0]], word[1:])
            else:
                for c in node.children:
                    if dfs(node.children[c], word[1:]):
                        return True
                return False
                
        
        return dfs(node, word)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)