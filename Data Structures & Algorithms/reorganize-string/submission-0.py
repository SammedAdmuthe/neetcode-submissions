class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter()

        for c in s:
            counter[c]+=1

        heap = []
        for c, count in counter.items():
            heapq.heappush(heap, (-count, 0, c))
        
        res = []

        while heap:
            count, recency, char = heapq.heappop(heap)
            if res and res[-1] == char:
                if not heap:
                    return ""
                count2, _, char2 = heapq.heappop(heap)
                res.append(char2)
                count2 +=1
                if -1 * count2:
                    heapq.heappush(heap, (count2, recency+1, char2))
                heapq.heappush(heap, (count, recency, char))
            else:
                res.append(char)
                count +=1
                if -1 * count:
                    heapq.heappush(heap, (count, recency+1, char))

        return "".join(res)