class MyCalendarTwo:
    def __init__(self):
        self.events = []
        self.doubled = []

    def book(self, startTime, endTime):
        for left, right in self.doubled:
            if max(left, startTime) < min(right, endTime):
                return False
        for left, right in self.events:
            overlap_start = max(left, startTime)
            overlap_end = min(right, endTime)
            if overlap_start < overlap_end:
                self.doubled.append((overlap_start, overlap_end))
        self.events.append((startTime, endTime))
        return True
