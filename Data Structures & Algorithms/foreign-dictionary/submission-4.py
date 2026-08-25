class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = defaultdict(list)
        indegree = {}
        for w in words:
            for c in w:
                graph[c] = []
                indegree[c] = 0

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            l1, l2 = 0, 0
            while l1 < len(w1) and l2 < len(w2) and w1[l1] == w2[l2]:
                l1+=1
                l2+=1

            if l1 < len(w1) and l2 < len(w2):
                graph[w1[l1]].append(w2[l2])
                indegree[w2[l2]]+=1
            elif l1 < len(w1):
                return ""
        
        q = deque()
        for key, val in indegree.items():
            if val == 0:
                q.append(key)
        
        print(q)
        seen = set()
        res = []
        def bfs():
            while q:
                popped = q.popleft()
                if popped in seen:
                    return ""
                res.append(popped)
                seen.add(popped)
                for neigh in graph[popped]:
                    indegree[neigh]-=1
                    if not indegree[neigh]:
                        q.append(neigh)


        bfs()
        if len(seen) != len(graph):
            return ""
        return "".join(res)
            
