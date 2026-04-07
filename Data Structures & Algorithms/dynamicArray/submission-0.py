class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = []
        self.cap = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self.array.append(n)
        self.cap = len(self.array)

    def popback(self) -> int:
        return self.array.pop()

    def resize(self) -> None:
        self.cap *= 2

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.cap