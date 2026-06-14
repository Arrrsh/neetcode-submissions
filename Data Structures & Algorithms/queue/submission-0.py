class Deque:
    
    def __init__(self):
        self.queue = []

    def isEmpty(self) -> bool:
        return len(self.queue) == 0
        

    def append(self, value: int) -> None:
        self.queue.append(value)

    def appendleft(self, value: int) -> None:
        self.queue.insert(0, value)

    def pop(self) -> int:
        if len(self.queue) > 0:
            v = self.queue[-1]
            del self.queue[-1]
            return v
        return -1

    def popleft(self) -> int:
        tmp = []
        if len(self.queue) > 0:
            v = self.queue[0]
            for i in range(len(self.queue) - 1):
                tmp.append(self.queue[i + 1])
            self.queue = tmp
            return v
        return -1
