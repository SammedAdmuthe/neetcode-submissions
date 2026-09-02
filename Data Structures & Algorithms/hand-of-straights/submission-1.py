class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand_counts = Counter(hand)
        heap = [ (hand, count) for hand, count in hand_counts.items()]
        heapq.heapify(heap)
        while heap:
            curr_hand, curr_count = heap[0]
            
            for i in range(curr_hand, curr_hand+groupSize):
                if i not in hand_counts:
                    return False
                hand_counts[i] -= 1
                if not hand_counts[i]:
                    if heap[0][0] != i:
                        return False
                    heapq.heappop(heap)

        return True