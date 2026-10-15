class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for x, y in sorted(tickets, reverse=True):
            graph[x].append(y)

        res = []
        def postTravesal(i):

            while graph[i]:
                node = graph[i].pop()
                postTravesal(node)
            res.append(i)

        postTravesal("JFK")
        return res[::-1]