class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u, v, p in flights:
            graph[u].append((v, p))

        heap = [(0, src, -1)]
        seen = set()
        while heap:

            cost, city, stops  = heapq.heappop(heap)

            if city == dst:
                return cost

            if (city, stops) in seen:
                continue

            seen.add((city, stops))
            if stops == k:
                continue
            for neigh, neigh_cost in graph[city]:

                if (neigh, stops + 1) in seen:
                    continue
                heapq.heappush(heap, (cost+neigh_cost, neigh, stops+1))

        return -1