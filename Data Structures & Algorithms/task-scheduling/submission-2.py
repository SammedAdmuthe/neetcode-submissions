class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
            X - 3
            Y - 2

            we must select the task that is more frequent
            X - 2
            Y - 2

            [(X, curr+n),(Y, curr+n)]
        '''

        task_freq = Counter(tasks)
        heap = []
        for task, freq in task_freq.items():
            heapq.heappush(heap, (-freq))

        q = deque()
        time = 0
        while heap or q:
            if heap:
                freq = -heapq.heappop(heap)
                if freq - 1:
                    freq-=1
                    q.append((freq, time + n))
            else:
                time = q[0][1]

            if q and time >= q[0][1]:
                heapq.heappush(heap, -q.popleft()[0])
            time+=1
        return time
            
            