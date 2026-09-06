class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        ta, tb, tc = target
        max_a, max_b, max_c = 0, 0, 0
        for a, b, c in triplets:
            if a > ta or b > tb or c > tc:
                continue
            
            max_a, max_b, max_c = max(max_a, a), max(max_b, b), max(max_c, c)
            
        return (max_a == ta and max_b == tb and max_c == tc)