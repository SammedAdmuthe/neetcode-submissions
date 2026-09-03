class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        N = len(points)
        adj = { i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)

                adj[i].append((dist,j))
                adj[j].append((dist,i))

        res = 0
        seen = set()
        heap= [(0, 0)]
        while len(seen) < N:

            cost, node = heapq.heappop(heap)

            if node in seen:
                continue

            res += cost
            seen.add(node)
            for neigh_cost, neigh in adj[node]:
                if neigh in seen:
                    continue

                heapq.heappush(heap, (neigh_cost, neigh))

        return res