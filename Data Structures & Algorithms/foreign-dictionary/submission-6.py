class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c : set() for w in words for c in w}
        n = len(words)

        for i in range(n):
            for j in range(i+1, n):

                # if words[i][k] not in graph:
                #     graph[words[i][k]] = set()
                # if words[j][k] not in graph:
                #     graph[words[j][k]] = set()
                # find the first non matching character
                k = 0
                while k < len(words[i]) and k < len(words[j]) and words[i][k] == words[j][k]:
                    k+=1
                
                if k < len(words[i]) and k < len(words[j]):
                    graph[words[i][k]].add(words[j][k])
                elif k < len(words[i]):
                    return ""


        in_degree = defaultdict(int)

        for node in graph:
            if node not in in_degree:
                in_degree[node] = 0
            for neigh in graph[node]:
                in_degree[neigh] += 1
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



        print(graph)
        return "".join(res) if len(seen) == len(graph) else ""
