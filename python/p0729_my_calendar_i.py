from bisect import bisect_left


class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, startTime, endTime):
        index = bisect_left(self.events, (startTime, endTime))
        if index and self.events[index - 1][1] > startTime:
            return False
        if index < len(self.events) and self.events[index][0] < endTime:
            return False
        self.events.insert(index, (startTime, endTime))
        return True
