class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize 

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)
    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1
    def increment(self, k: int, val: int) -> None:
        for i,j in enumerate(self.stack[:k]):
            self.stack[i] += val