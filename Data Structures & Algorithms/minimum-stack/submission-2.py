class MinStack:

    def __init__(self):
        self.stack = []
        self.minE = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minE) != 0:
            self.minE.append(min(val, self.minE[-1]))
        else:
            self.minE.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minE.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minE) == 0:
            return None
        return self.minE[-1]
