class TrieNode():
    def __init__(self):
        self.nodes = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.nodes:
                curr.nodes[w] = TrieNode()
            curr = curr.nodes[w]
        curr.is_word = True

    def matchRest(self, indx, curr, word):
        if indx == len(word):
            return curr.is_word

        if word[indx] == '.':
            for node in curr.nodes:
                if self.matchRest(indx+1, curr.nodes[node], word):
                    return True

        elif word[indx] not in curr.nodes:
            return False

        else:
            if self.matchRest(indx+1, curr.nodes[word[indx]], word):
                return True
        
        return False

        



    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            w = word[i]
            if w == '.':
                return self.matchRest(i, curr, word)

            if w not in curr.nodes:
                return False
            curr = curr.nodes[w]
        return curr.is_word
