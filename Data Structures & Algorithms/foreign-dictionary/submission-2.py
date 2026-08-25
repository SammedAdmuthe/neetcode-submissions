class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = defaultdict(list)
        for w in words:
            for c in w:
                graph[c] = []
            
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            l1, l2 = 0, 0
            while l1 < len(w1) and l2 < len(w2) and w1[l1] == w2[l2]:
                l1+=1
                l2+=1

            if l1 < len(w1) and l2 < len(w2):
                graph[w1[l1]].append(w2[l2])
            elif l1 < len(w1):
                return ""

        res = []
        def dfs(v):
            if v in seen:
                return seen[v]

            seen[v] = True
            for neigh in graph[v]:
                if dfs(neigh):
                    return True
                
            seen[v] = False
            res.append(v)
            
            return False

        seen = {}
        for v in graph:
            if dfs(v):
                return ""
        
        
        res.reverse()
        return "".join(res)
            
