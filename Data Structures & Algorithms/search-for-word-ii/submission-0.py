class TrieNode:

    def __init__(self):
        self.nodes = {}
        self.is_word = False
    
    def insert(self, word):
        curr = self

        for w in word:
            if w not in curr.nodes:
                curr.nodes[w] = TrieNode()

            curr = curr.nodes[w]
        curr.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        res = set()
        seen = set()
        
        def dfs(r, c, node, s):
            if r < 0 or r >= m or c < 0 or c >=n or (r, c) in seen or board[r][c] not in node.nodes:
                return
            

            node = node.nodes[board[r][c]]
            s += board[r][c]
            if node.is_word:
                res.add(s)

            seen.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r+dr, c+dc, node, s)

            seen.remove((r, c))
    

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")

        return list(res)