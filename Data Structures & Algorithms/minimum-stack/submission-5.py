class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_v = None
        if self.stack:
            min_v = min(val, self.stack[-1][1])
        else:
            min_v = val
        self.stack.append((val, min_v))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None
        
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None
        
