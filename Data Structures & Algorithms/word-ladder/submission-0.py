class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''

            cat -> bat -> bag -> sag

        '''

        graph = defaultdict(list)
        n = len(wordList)
        def differByOne(word1, word2):
            x, y = 0, 0
            count = 0
            while x < len(word1) and y < len(word2):
                if word1[x] != word2[y]:
                    count +=1
                x+=1
                y+=1

            if x < len(word1):
                count += (len(word1) - x)
            if y < len(word2):
                count += (len(word2) - y)

            return count == 1
        
        for i in range(n):
            for j in range(i+1, n):
                if differByOne(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])


        for i in range(n):
            if differByOne(beginWord, wordList[i]):
                graph[beginWord].append(wordList[i])
                graph[wordList[i]].append(beginWord)

        print(graph)
        

        q = deque()

        q.append((beginWord, 1))
        seen = set()

        while q:
            word, cost = q.popleft()

            if word == endWord:
                return cost
            seen.add(word)
            
            for neigh in graph[word]:
                if neigh in seen:
                    continue
                q.append((neigh, cost + 1))

        return 0

        