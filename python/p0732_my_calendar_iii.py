class MyCalendarThree:
    def __init__(self):
        self.changes = {}

    def book(self, startTime, endTime):
        self.changes[startTime] = self.changes.get(startTime, 0) + 1
        self.changes[endTime] = self.changes.get(endTime, 0) - 1
        active = maximum = 0
        for point in sorted(self.changes):
            active += self.changes[point]
            maximum = max(maximum, active)
        return maximum
