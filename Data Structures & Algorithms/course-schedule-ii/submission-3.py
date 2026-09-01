class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()

        '''
            [a, b] -> 
            
            b -> a
        '''
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        for course in range(numCourses):
            if not indegree[course]:
                q.append(course)

        res = []
        seen = set()
        while q:
            course = q.popleft()
            if course not in seen:
                res.append(course)
            seen.add(course)

            for neigh in graph[course]:
                if neigh in seen or not indegree[neigh]:
                    continue
                indegree[neigh] -= 1

                if not indegree[neigh]:
                    q.append(neigh)

        return res if len(seen) == numCourses else []
                

        