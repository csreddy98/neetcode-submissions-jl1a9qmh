class TrieNode():
    def __init__(self):
        self.chars = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.chars:
                node.chars[c] = TrieNode()
            node = node.chars[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.chars.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.chars:
                        return False
                    cur = cur.chars[c]
            return cur.isEnd
                
        return dfs(0, self.root)
