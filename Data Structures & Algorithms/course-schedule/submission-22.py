class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        seen = set()
        path = set()
        def hasCycle(i, par):

            if i in path:
                return True
            if i in seen:
                return False

            seen.add(i)
            path.add(i)
            for neigh in graph[i]:
                if hasCycle(neigh, i):
                    return True
            path.remove(i)
            return False
                
        for i in range(numCourses):
            if hasCycle(i, -1):
                return False

        return True