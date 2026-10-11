class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        for i, weight in enumerate(w):
            for j in range(weight):
                self.arr.append(i)

    def pickIndex(self) -> int:
        rand = random.randrange(0, len(self.arr))
        return self.arr[rand]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()