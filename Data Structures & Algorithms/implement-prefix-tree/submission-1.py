class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.chars:
                node.chars[c] = TrieNode()
            node = node.chars[c]
        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.chars:
                return False
            node = node.chars[c]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.chars:
                return False
            node = node.chars[c]
        return True
        
        