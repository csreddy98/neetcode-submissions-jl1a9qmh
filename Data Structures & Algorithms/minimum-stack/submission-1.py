class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.minimum:
            tmp = []
            new_min = float("inf")
            while len(self.stack):
                new_min = min(new_min, self.stack[-1])
                tmp.append(self.stack.pop())
            self.minimum = new_min
            while len(tmp):
                self.stack.append(tmp.pop())
        return value

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
