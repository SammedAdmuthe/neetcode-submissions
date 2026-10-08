class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # stack = [(price, count)]
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            popped_price, popped_count = self.stack.pop()
            count += popped_count
        
        self.stack.append((price, count))
        return count 



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)