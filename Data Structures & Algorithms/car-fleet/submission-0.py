class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''

                target miles = 10
                
                6 left miles -> 3hr
                8 left mile -> 4hr
                10 left mile -> 10hr
                4 left -> 4hr


        '''

        heap = [(-pos, (target - pos)/speed) for pos, speed in zip(position, speed)]
        heapq.heapify(heap)

        fleet = 0
        while heap:
            pos, time = heapq.heappop(heap)

            fleet+=1
            while heap and heap[0][1] <= time:
                heapq.heappop(heap)
        
        return fleet





