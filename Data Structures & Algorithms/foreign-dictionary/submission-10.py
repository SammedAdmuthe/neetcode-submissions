class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c : set() for w in words for c in w}
        in_degree = {c: 0 for c in graph}
        n = len(words)

        for i in range(1, n):
                k = 0
                while k < len(words[i-1]) and k < len(words[i]) and words[i-1][k] == words[i][k]:
                    k+=1
                
                if k < len(words[i-1]) and k < len(words[i]) and words[i][k] not in graph[words[i-1][k]]:
                    graph[words[i-1][k]].add(words[i][k])
                    in_degree[words[i][k]] +=1
                elif  k >= len(words[i]) and k < len(words[i-1]):
                    return ""

        q = deque()
        for node in in_degree.keys():
            if not in_degree[node]:
                q.append(node)

        seen = set()
        res = []
        while q:

            curr = q.popleft()
            if curr in seen:
                continue

            seen.add(curr)
            res.append(curr)

            for neigh in graph[curr]:
                in_degree[neigh] -=1
                if not in_degree[neigh]:
                    q.append(neigh)



        return "".join(res) if len(seen) == len(graph) else ""
