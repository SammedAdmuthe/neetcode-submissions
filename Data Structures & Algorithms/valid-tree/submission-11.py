class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)


        seen = set()
        def hasCycle(node, par):
            if node in seen:
                return True


            seen.add(node)
            for neigh in graph[node]:
                # 1 - 2 - 3 -  1
                if neigh == par:
                    continue
                else:
                    if hasCycle(neigh, node):
                        return True

            return False

        if hasCycle(0, -1):
            return False
        print(seen)

        return len(seen) == n
