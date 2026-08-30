class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graph = defaultdict(list)

        for c1, c2 in prerequisites:
            graph[c2].append(c1)

        
        def hasCycle(indx):
            if indx in path:
                return True

            if indx in seen:
                return False

            seen.add(indx)
            path.add(indx)
            for neigh in graph[indx]:
                if hasCycle(neigh):
                    return True
            path.remove(indx)
            return False
        
        seen = set()
        for i in range(numCourses):
            path = set()
            if hasCycle(i):
                return False
        
        return True