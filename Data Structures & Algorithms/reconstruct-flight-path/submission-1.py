class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
            A->B->C->D
                  |
                  E

            A B C, E, C, D
        """
        graph = defaultdict(list)
        for u, v in sorted(tickets, reverse = True):
            graph[u].append(v)

        res = deque()
        def post_order(node):
            while graph[node]:
                dst = graph[node].pop()
                post_order(dst)
            res.appendleft(node)


        
        post_order("JFK")

        return list(res)