class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            _, min_ = self.stack[-1]
            self.stack.append((val, min(val, min_)))
            return
        self.stack.append((val, val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
            
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        
