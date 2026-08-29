
class TrieNode:
    def __init__(self):
        self.node = {}# a - z -> TrieNode
        self.is_word = False


class PrefixTree:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head

        for w in word:
            if w not in curr.node:
                curr.node[w] = TrieNode()
            curr = curr.node[w]
        curr.is_word = True

            

    def search(self, word: str) -> bool:
        curr = self.head

        for w in word:
            if w not in curr.node:
                return False
            curr = curr.node[w]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.head

        for w in prefix:
            if w not in curr.node:
                return False
            curr = curr.node[w]
        return True