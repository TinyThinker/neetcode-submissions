import heapq
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            new_min = min(val, self.stack[-1][1])
            self.stack.append((val, new_min))
        
    def pop(self) -> None:
        if not self.stack:
            return None
        else:
            return self.stack.pop()[0]

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][0]
        
    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][1]
        
