class Solution:
    def carPooling(self, trips, capacity):
        changes = {}
        for passengers, start, end in trips:
            changes[start] = changes.get(start, 0) + passengers
            changes[end] = changes.get(end, 0) - passengers
        aboard = 0
        for position in sorted(changes):
            aboard += changes[position]
            if aboard > capacity:
                return False
        return True
