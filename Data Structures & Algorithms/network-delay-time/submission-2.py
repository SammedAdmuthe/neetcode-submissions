

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        seen = set()
        while heap:
            t, node = heapq.heappop(heap)
            if node in seen:
                continue

            seen.add(node)
            if len(seen) == n:
                return t

            for neigh, neigh_time in graph[node]:

                if neigh in seen:
                    continue
                heapq.heappush(heap, (t + neigh_time, neigh))

        return -1


                