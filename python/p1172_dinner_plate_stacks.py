from heapq import heappop, heappush


class DinnerPlates:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.available = []

    def push(self, val):
        while self.available and (self.available[0] >= len(self.stacks)
                                  or len(self.stacks[self.available[0]]) == self.capacity):
            heappop(self.available)
        if not self.available:
            heappush(self.available, len(self.stacks))
            self.stacks.append([])
        index = self.available[0]
        self.stacks[index].append(val)
        if len(self.stacks[index]) == self.capacity:
            heappop(self.available)

    def pop(self):
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        was_full = len(self.stacks[index]) == self.capacity
        value = self.stacks[index].pop()
        if was_full:
            heappush(self.available, index)
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return value
