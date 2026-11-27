from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.frequency = defaultdict(int)
        self.groups = defaultdict(list)
        self.maximum = 0

    def push(self, val):
        self.frequency[val] += 1
        count = self.frequency[val]
        self.groups[count].append(val)
        self.maximum = max(self.maximum,count)

    def pop(self):
        val = self.groups[self.maximum].pop()
        self.frequency[val] -= 1
        if not self.groups[self.maximum]:
            self.maximum -= 1
        return val
