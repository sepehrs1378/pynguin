class Counter:
    def __init__(self) -> None:
        self.map = {}

    def add(self, x: int) -> None:
        if x in self.map:
            self.map[x] += 1
        else:
            self.map[x] = 1

    def remove(self, x: int) -> None:
        if x not in self.map:
            return
        self.map[x] -= 1
        if self.map[x] == 0:
            del self.map[x]

    def reset(self) -> None:
        self.map = {}
